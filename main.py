import os
import re
import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QMessageBox
from PySide6.QtCore import QFile, Slot, Signal, QObject, QThread
from PySide6.QtGui import QAction
from ui_mainwindow import Ui_MainWindow


#
# 在临时文件的处理上，没有生成temp文件以避免因为删除失败而产生内容泄露。
# 但是在某些极端情况下，可能由于大量数据写出导致 GUI HANG住。
#

textHelp = """教务处下载的名单：学生正选后，从教务处系统下载下来的选课表名单
BB课程及ID对照表：BB用于导入课程的表单
补选后下载的名单：学生补选后，从教务处系统下载下来的名单
"""


class Worker(QObject):
    finished = Signal()
    progress = Signal(int)
    output = Signal(str)
    content = Signal(object)

    def __init__(self, adf, bbdf):
        super().__init__()
        self.adf = adf
        self.bbdf = bbdf

    # 自定义日志输出,方便后期调试
    def logger(self, c):
        self.output.emit(c)

    def run(self):

        gdf = pd.DataFrame()

        try:
            adf = pd.read_excel(self.adf)
            bbdf = pd.read_excel(self.bbdf)
        except FileNotFoundError:
            self.logger("\n对照表文件未找到。请确保文件在选择的位置！\n")
            self.finished.emit()
            self.thread.quit()

        self.logger("\n开始处理...\n")

        # 全局变量

        # 用于存储课程注册信息的字典
        cc = {}

        csc = 0
        ccf = []
        ss = []
        logBuffer = ""

        # 生成一个字典用于存储川大课程号加课序号对应的BB课程ID。
        scbbdict = {}

        # 检查BB课程ID表文件格式
        try:
            for i, r in bbdf.iterrows():
                if len(str(r[2])) > 4:
                    continue
                if len(str(r[0])) != 9:
                    raise IndexError
                scbbdict[(str(r[0]), str(r[2]))] = r[4]

            if len(scbbdict) < 1:
                raise IndexError

        except IndexError:
            self.logger("BB课程ID表生成失败，请确保文件格式正确！")
            self.finished.emit()
            self.thread.quit()

        try:
            for i, r in adf.iterrows():
                if len(str(r[3])) > 4:
                    continue
                if len(str(r[2])) != 9:
                    raise IndexError

                scid = str(r[2])
                csec = str(r[3])

                if (scid, csec) not in scbbdict:
                    if logBuffer != str(r[4]) + "课程不在BB中":
                        logBuffer = str(r[4]) + "课程不在BB中"
                        self.logger(logBuffer)
                        ccf.append((str(r[4]), csec))
                    continue

                # ss.append((str(r[4]), scid, csec, str(scbbdict[(scid, csec)], r[0]))) #调试用
                # 课程号在前，学号在后
                ss.append((str(scbbdict[(scid, csec)]), str(r[0])))
                if str(r[4]) in cc:
                    if str(csec) in cc[str(r[4])]:
                        cc[str(r[4])][str(csec)] += 1
                    else:
                        cc[str(r[4])][str(csec)] = 0
                else:
                    cc[str(r[4])] = {}
                csc += 1
                self.progress.emit(i / len(adf.index) * 100)

            gdf = pd.concat([gdf, pd.DataFrame(ss)], ignore_index=True)

            self.content.emit(gdf)

            self.logger("\n" + str(len(set(cc.keys()))) +
                        " 门课程已处理完成。" + "共计 " + str(csc) + " 人次注册。\n")
            for k in cc:
                for i in cc[k]:
                    self.logger(k + ": " + str(i) + ": " + str(cc[k][i]))
            if len(ccf):
                self.logger("\n其中，" + str(len(set(ccf))) + " 门课程处理失败: ")
                for c in set(ccf):
                    self.logger(c[0] + " " + ("课序号：" + c[1]) + "\n")

            self.progress.emit(100)
            self.finished.emit()

        except IndexError:
            self.logger("教务处下载的名单出错，课程ID不正确，请确保文件格式及内容正确！")
            self.finished.emit()
            self.thread.quit()


class Comparer(QObject):
    finished = Signal()
    progress = Signal(int)
    output = Signal(str)
    content1 = Signal(object)
    content2 = Signal(object)

    def __init__(self, file1, file2):
        super().__init__()
        self.file1 = file1
        self.file2 = file2

    # 自定义日志输出,方便后期调试
    def logger(self, c):
        self.output.emit(c)

    def run(self):
        self.logger("开始比较差异...")

        # if pd.DataFrame().compare(self.file1):
        #     self.finished.emit()
        # if pd.DataFrame().compare(self.file2):
        #     self.finished.emit()

        df1 = self.file1
        df2 = self.file2

        la = set([])
        lanew = set([])

        diffadd = []
        diffrem = []

        # r[0] BB课程ID， r[1] 学号
        for i, r in df1.iterrows():
            la.add((r[0], r[1]))

        self.progress.emit(20)

        for i, r in df2.iterrows():
            lanew.add((r[0], r[1]))

        self.progress.emit(40)

        # 新的名单里有的,而旧的名单里没有的,就是要添加的
        diffadd = list(lanew - la)

        # 新的名单里没有的,而旧的名单里有的,就是要删除的
        diffrem = list(la - lanew)

        dfadd = pd.DataFrame()
        dfrem = pd.DataFrame()

        if (len(diffadd) > 0):
            dfadd = pd.concat(
                [dfadd, pd.DataFrame(diffadd)], ignore_index=True)
            self.content1.emit(dfadd)
        else:
            self.logger("没有新增的差异！")
        if (len(diffrem) > 0):
            dfrem = pd.concat(
                [dfrem, pd.DataFrame(diffrem)], ignore_index=True)
            self.content2.emit(dfrem)
        else:
            self.logger("没有删减的差异！")

        self.finished.emit()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.adf = ""
        self.bbdf = ""
        self.andf = ""
        self.ofile = ""
        self.ofileadd = ""
        self.ofilerem = ""

        self.aboutAction = QAction('&关于', self)
        self.aboutText = """程序版本：1.2\nfrederich.liu@scupi.cn\nAll rights reserved\n2021-01-20"""
        self.aboutAction.triggered.connect(
            lambda: self.showDialog(self.aboutText))

        # 添加事件
        self.ui.checkBox.stateChanged.connect(self.updateState)
        self.ui.pushButton_jwc.clicked.connect(lambda: self.chooseFile("all"))
        self.ui.pushButton_bb.clicked.connect(lambda: self.chooseFile("bb"))
        self.ui.pushButton_jwc_new.clicked.connect(
            lambda: self.chooseFile("all-new"))
        self.ui.pushButton_start.clicked.connect(self.saveFile)
        self.ui.pushButton_start.clicked.connect(self.genData)

        self.ui.menuBar.addAction(self.aboutAction)

        # 初始化日志窗口
        self.logger(u"程序已就绪，请选择文件进行处理。")
        self.logger(textHelp)

        self.updateSb(u"请选择文件以运行程序")

    def logger(self, c):
        return self.ui.textBrowser.append(c)

    def updateSb(self, c):
        return self.ui.statusbar.showMessage(c)

    def showDialog(self, text):
        msgbox = QMessageBox()
        msgbox.setWindowTitle(u'关于')
        msgbox.setText(text)
        msgbox.exec_()

    def updateState(self):
        if self.ui.checkBox.isChecked():
            self.ui.lineEdit_jwc_new.setEnabled(True)
            self.ui.pushButton_jwc_new.setEnabled(True)
            self.ui.pushButton_start.clicked.disconnect(self.genData)
            self.ui.pushButton_start.clicked.connect(self.genComp)
        else:
            self.andf = ""
            self.ui.lineEdit_jwc_new.setText("")
            self.ui.lineEdit_jwc_new.setEnabled(False)
            self.ui.pushButton_jwc_new.setEnabled(False)
            self.ui.pushButton_start.clicked.disconnect(self.genComp)
            self.ui.pushButton_start.clicked.connect(self.genData)
        self.updateButton()

    def chooseFile(self, bname):
        fileName, _ = QFileDialog.getOpenFileName(self,
                                                  "选择xlsx文件", "", "Excel文件 (*.xlsx)")

        if bname == "all":
            if fileName:
                self.adf = fileName
                self.ui.lineEdit_jwc.setText(fileName)
            else:
                self.adf = ""
                self.ui.lineEdit_jwc.setText("")
            self.updateButton()
            return
        if bname == "bb":
            if fileName:
                self.bbdf = fileName
                self.ui.lineEdit_bb.setText(fileName)
            else:
                self.bbdf = ""
                self.ui.lineEdit_bb.setText("")
            self.updateButton()
            return
        if bname == "all-new":
            if fileName:
                self.andf = fileName
                self.ui.lineEdit_jwc_new.setText(fileName)
            else:
                self.andf = ""
                self.ui.lineEdit_jwc_new.setText("")
            self.updateButton()
            return

    def saveFile(self):
        fileName, _ = QFileDialog.getSaveFileName(self,
                                                  "选择输出文件名", "", "CVS文件 (*.csv)")
        if fileName:
            self.ofile = fileName
            if self.ui.checkBox.isChecked():
                (pname, ext) = os.path.splitext(fileName)
                self.ofileadd = pname + "-新增名单" + ext
                self.ofilerem = pname + "-删减名单" + ext
                self.logger(u"新增学生名单将保存为：" + self.ofileadd)
                self.logger(u"删减学生名单将保存为：" + self.ofilerem)
            else:
                self.logger(u"注册名单将保存为：" + fileName)
        else:
            self.ofile = ""
            self.logger("用户取消操作")

    def updateButton(self):
        if self.adf and self.bbdf and not (bool(self.ui.checkBox.isChecked()) != bool(self.andf)):
            self.ui.pushButton_start.setEnabled(True)
        else:
            self.ui.pushButton_start.setEnabled(False)

    def writeFile(self, content, path):
        try:
            content.to_csv(path, index=False, header=False,
                           encoding='utf_8_sig')
        except PermissionError:
            self.logger("文件写入失败，请检查是否已经打开了同目录下的同名文件！")

    @Slot()
    def genData(self):

        if self.ofile == "":
            return

        self.thread = QThread()
        self.worker = Worker(self.adf, self.bbdf)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.updateSb(u"正在处理数据")
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.worker.finished.connect(lambda: self.updateSb(u"处理完成"))
        self.worker.finished.connect(
            lambda: self.logger(u"数据处理完成，请检查生成的文件。\n"))
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(lambda p: self.ui.progressBar.setValue(p))
        self.worker.output.connect(lambda c: self.logger(c))

        self.worker.content.connect(
            lambda content: self.writeFile(content, self.ofile)
        )

        self.thread.start()

        self.ui.pushButton_start.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.ui.pushButton_start.setEnabled(True)
        )

    @Slot()
    def genComp(self):

        if self.ofile == "":
            return

        self.file1 = pd.DataFrame()
        self.file2 = pd.DataFrame()

        def updateFile(f, id):
            if id == 1:
                self.file1 = f
            if id == 2:
                self.file2 = f

        self.p = 0
        self.lock1 = False
        self.lock2 = False

        def checkLock(i):
            if i == 1:
                self.lock1 = True
            if i == 2:
                self.lock2 = True

            if self.lock1 and self.lock2:
                self.updateSb(u"正在处理数据")
                self.th3 = QThread()
                self.comp = Comparer(self.file1, self.file2)
                self.comp.moveToThread(self.th3)
                self.th3.started.connect(self.comp.run)
                self.comp.finished.connect(self.th3.quit)
                self.comp.finished.connect(self.comp.deleteLater)
                self.th3.finished.connect(self.th3.deleteLater)
                self.comp.progress.connect(lambda p: up(p))
                self.comp.output.connect(lambda c: self.logger(c))
                self.comp.content1.connect(
                    lambda content: self.writeFile(content, self.ofileadd)
                )
                self.comp.content2.connect(
                    lambda content: self.writeFile(content, self.ofilerem)
                )
                self.th3.finished.connect(
                    lambda: self.ui.progressBar.setValue(100)
                )
                self.comp.finished.connect(
                    lambda: self.logger(u"数据处理完成，请检查生成的文件。\n")
                )
                self.comp.finished.connect(
                    lambda: self.updateSb(u"处理完成")
                )
                self.th3.finished.connect(
                    lambda: self.ui.pushButton_start.setEnabled(True)
                )
                self.th3.start()

        def up(wp):
            self.p += 0.4 * wp
            self.ui.progressBar.setValue(self.p)

        self.th1 = QThread()
        self.th2 = QThread()

        self.worker1 = Worker(self.adf, self.bbdf)
        self.worker2 = Worker(self.andf, self.bbdf)

        self.worker1.moveToThread(self.th1)
        self.worker2.moveToThread(self.th2)

        self.th1.started.connect(self.worker1.run)
        self.worker1.content.connect(
            lambda f: updateFile(f, 1)
        )
        self.worker1.finished.connect(self.th1.quit)
        self.worker1.finished.connect(self.worker1.deleteLater)
        self.worker1.finished.connect(lambda: checkLock(1))
        self.th1.finished.connect(self.th1.deleteLater)

        self.th2.started.connect(self.worker2.run)
        self.worker2.content.connect(
            lambda f: updateFile(f, 2)
        )
        self.worker2.finished.connect(self.th2.quit)
        self.worker2.finished.connect(self.worker2.deleteLater)
        self.worker2.finished.connect(lambda: checkLock(2))
        self.th2.finished.connect(self.th2.deleteLater)

        self.worker1.progress.connect(lambda p: up(p))
        self.worker2.progress.connect(lambda p: up(p))

        # self.worker1.output.connect(lambda c: self.logger(c))
        # self.worker2.output.connect(lambda c: self.logger(c))

        self.th1.start()
        self.th2.start()

        self.ui.pushButton_start.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
