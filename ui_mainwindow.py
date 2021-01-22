# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 450)
        MainWindow.setMinimumSize(QSize(600, 450))
        icon = QIcon()
        icon.addFile(u":/icos/ico.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_desc = QLabel(self.centralwidget)
        self.label_desc.setObjectName(u"label_desc")

        self.horizontalLayout_2.addWidget(self.label_desc)

        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_2.addWidget(self.checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_bb = QLineEdit(self.centralwidget)
        self.lineEdit_bb.setObjectName(u"lineEdit_bb")
        self.lineEdit_bb.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_bb, 1, 1, 1, 1)

        self.pushButton_jwc = QPushButton(self.centralwidget)
        self.pushButton_jwc.setObjectName(u"pushButton_jwc")

        self.gridLayout.addWidget(self.pushButton_jwc, 0, 2, 1, 1)

        self.pushButton_bb = QPushButton(self.centralwidget)
        self.pushButton_bb.setObjectName(u"pushButton_bb")

        self.gridLayout.addWidget(self.pushButton_bb, 1, 2, 1, 1)

        self.label_jwc_new = QLabel(self.centralwidget)
        self.label_jwc_new.setObjectName(u"label_jwc_new")

        self.gridLayout.addWidget(self.label_jwc_new, 2, 0, 1, 1)

        self.label_bb = QLabel(self.centralwidget)
        self.label_bb.setObjectName(u"label_bb")

        self.gridLayout.addWidget(self.label_bb, 1, 0, 1, 1)

        self.label_jwc = QLabel(self.centralwidget)
        self.label_jwc.setObjectName(u"label_jwc")

        self.gridLayout.addWidget(self.label_jwc, 0, 0, 1, 1)

        self.lineEdit_jwc = QLineEdit(self.centralwidget)
        self.lineEdit_jwc.setObjectName(u"lineEdit_jwc")
        self.lineEdit_jwc.setReadOnly(True)
        self.lineEdit_jwc.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.lineEdit_jwc, 0, 1, 1, 1)

        self.lineEdit_jwc_new = QLineEdit(self.centralwidget)
        self.lineEdit_jwc_new.setObjectName(u"lineEdit_jwc_new")
        self.lineEdit_jwc_new.setEnabled(False)
        self.lineEdit_jwc_new.setAutoFillBackground(False)
        self.lineEdit_jwc_new.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_jwc_new, 2, 1, 1, 1)

        self.pushButton_jwc_new = QPushButton(self.centralwidget)
        self.pushButton_jwc_new.setObjectName(u"pushButton_jwc_new")
        self.pushButton_jwc_new.setEnabled(False)

        self.gridLayout.addWidget(self.pushButton_jwc_new, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.pushButton_start = QPushButton(self.centralwidget)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setEnabled(False)
        font = QFont()
        font.setPointSize(15)
        self.pushButton_start.setFont(font)

        self.verticalLayout.addWidget(self.pushButton_start)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 578, 194))
        self.horizontalLayout = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textBrowser = QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout.addWidget(self.textBrowser)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 600, 22))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u751f\u6210\u5b66\u751f\u540d\u5355", None))
        self.label_desc.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u5148\u9009\u62e9excel\u6587\u4ef6\uff1a", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u5dee\u5f02\u540d\u5355", None))
        self.pushButton_jwc.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6...", None))
        self.pushButton_bb.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6...", None))
        self.label_jwc_new.setText(QCoreApplication.translate("MainWindow", u"\u8865\u9009\u540e\u4e0b\u8f7d\u7684\u540d\u5355\uff1a", None))
        self.label_bb.setText(QCoreApplication.translate("MainWindow", u"BB\u8bfe\u7a0b\u53caID\u5bf9\u7167\u8868\uff1a", None))
        self.label_jwc.setText(QCoreApplication.translate("MainWindow", u"\u6559\u52a1\u5904\u4e0b\u8f7d\u7684\u540d\u5355\uff1a", None))
        self.lineEdit_jwc.setText("")
        self.pushButton_jwc_new.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6...", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u70b9\u51fb\u751f\u6210", None))
    # retranslateUi

