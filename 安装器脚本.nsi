; 该脚本使用 HM VNISEdit 脚本编辑器向导产生

; 安装程序初始定义常量
!define PRODUCT_NAME "学生注册名单生成器"
!define PRODUCT_VERSION "1.2"
!define PRODUCT_PUBLISHER "SCUPI"
!define PRODUCT_WEB_SITE "https://support.scupi.cn"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\Generator.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"

SetCompressor lzma

; ------ MUI 现代界面定义 (1.67 版本以上兼容) ------
!include "MUI.nsh"

; MUI 预定义常量
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"

; 欢迎页面
!insertmacro MUI_PAGE_WELCOME
; 许可协议页面
!insertmacro MUI_PAGE_LICENSE "License.txt"
; 安装目录选择页面
!insertmacro MUI_PAGE_DIRECTORY
; 安装过程页面
!insertmacro MUI_PAGE_INSTFILES
; 安装完成页面
!define MUI_FINISHPAGE_RUN "$INSTDIR\Generator.exe"
!insertmacro MUI_PAGE_FINISH

; 安装卸载过程页面
!insertmacro MUI_UNPAGE_INSTFILES

; 安装界面包含的语言设置
!insertmacro MUI_LANGUAGE "SimpChinese"

; 安装预释放文件
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS
; ------ MUI 现代界面定义结束 ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "Setup.exe"
InstallDir "$PROGRAMFILES\学生注册名单生成器"
InstallDirRegKey HKLM "${PRODUCT_UNINST_KEY}" "UninstallString"
ShowInstDetails show
ShowUnInstDetails show
BrandingText "学生注册名单生成器"

Section "MainSection" SEC01
  SetOutPath "$INSTDIR"
  SetOverwrite ifnewer
  File /r "dist\Generator\*.*"
  CreateDirectory "$SMPROGRAMS\学生注册名单生成器"
  CreateShortCut "$SMPROGRAMS\学生注册名单生成器\学生注册名单生成器.lnk" "$INSTDIR\Generator.exe"
  CreateShortCut "$DESKTOP\学生注册名单生成器.lnk" "$INSTDIR\Generator.exe"
  File "dist\Generator\VCRUNTIME140_1.dll"
  File "dist\Generator\VCRUNTIME140.dll"
  File "dist\Generator\unicodedata.pyd"
  File "dist\Generator\sqlite3.dll"
  File "dist\Generator\shiboken6.abi3.dll"
  File "dist\Generator\select.pyd"
  File "dist\Generator\Qt6Widgets.dll"
  File "dist\Generator\Qt6Qml.dll"
  File "dist\Generator\Qt6Network.dll"
  File "dist\Generator\Qt6Gui.dll"
  File "dist\Generator\Qt6Core.dll"
  File "dist\Generator\python39.dll"
  File "dist\Generator\python3.dll"
  File "dist\Generator\pyside6.abi3.dll"
  File "dist\Generator\pyexpat.pyd"
  File "dist\Generator\MSVCP140_1.dll"
  File "dist\Generator\MSVCP140.dll"
  File "dist\Generator\libssl-1_1.dll"
  File "dist\Generator\libopenblas.WCDJNK7YVMPZQ2ME2ZZHJJRJ3JIKNDB7.gfortran-win_amd64.dll"
  File "dist\Generator\libffi-7.dll"
  File "dist\Generator\libcrypto-1_1.dll"
  File "dist\Generator\Generator.exe.manifest"
  File "dist\Generator\Generator.exe"
  File "dist\Generator\base_library.zip"
  File "dist\Generator\_uuid.pyd"
  File "dist\Generator\_ssl.pyd"
  File "dist\Generator\_sqlite3.pyd"
  File "dist\Generator\_socket.pyd"
  File "dist\Generator\_queue.pyd"
  File "dist\Generator\_overlapped.pyd"
  File "dist\Generator\_multiprocessing.pyd"
  File "dist\Generator\_lzma.pyd"
  File "dist\Generator\_hashlib.pyd"
  File "dist\Generator\_elementtree.pyd"
  File "dist\Generator\_decimal.pyd"
  File "dist\Generator\_ctypes.pyd"
  File "dist\Generator\_bz2.pyd"
  File "dist\Generator\_asyncio.pyd"
SectionEnd

Section -AdditionalIcons
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateShortCut "$SMPROGRAMS\学生注册名单生成器\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\学生注册名单生成器\Uninstall.lnk" "$INSTDIR\uninst.exe"
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\Generator.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\Generator.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd

/******************************
 *  以下是安装程序的卸载部分  *
 ******************************/

Section Uninstall
  Delete "$INSTDIR\${PRODUCT_NAME}.url"
  Delete "$INSTDIR\uninst.exe"
  Delete "$INSTDIR\_asyncio.pyd"
  Delete "$INSTDIR\_bz2.pyd"
  Delete "$INSTDIR\_ctypes.pyd"
  Delete "$INSTDIR\_decimal.pyd"
  Delete "$INSTDIR\_elementtree.pyd"
  Delete "$INSTDIR\_hashlib.pyd"
  Delete "$INSTDIR\_lzma.pyd"
  Delete "$INSTDIR\_multiprocessing.pyd"
  Delete "$INSTDIR\_overlapped.pyd"
  Delete "$INSTDIR\_queue.pyd"
  Delete "$INSTDIR\_socket.pyd"
  Delete "$INSTDIR\_sqlite3.pyd"
  Delete "$INSTDIR\_ssl.pyd"
  Delete "$INSTDIR\_uuid.pyd"
  Delete "$INSTDIR\base_library.zip"
  Delete "$INSTDIR\Generator.exe"
  Delete "$INSTDIR\Generator.exe.manifest"
  Delete "$INSTDIR\libcrypto-1_1.dll"
  Delete "$INSTDIR\libffi-7.dll"
  Delete "$INSTDIR\libopenblas.WCDJNK7YVMPZQ2ME2ZZHJJRJ3JIKNDB7.gfortran-win_amd64.dll"
  Delete "$INSTDIR\libssl-1_1.dll"
  Delete "$INSTDIR\MSVCP140.dll"
  Delete "$INSTDIR\MSVCP140_1.dll"
  Delete "$INSTDIR\pyexpat.pyd"
  Delete "$INSTDIR\pyside6.abi3.dll"
  Delete "$INSTDIR\python3.dll"
  Delete "$INSTDIR\python39.dll"
  Delete "$INSTDIR\Qt6Core.dll"
  Delete "$INSTDIR\Qt6Gui.dll"
  Delete "$INSTDIR\Qt6Network.dll"
  Delete "$INSTDIR\Qt6Qml.dll"
  Delete "$INSTDIR\Qt6Widgets.dll"
  Delete "$INSTDIR\select.pyd"
  Delete "$INSTDIR\shiboken6.abi3.dll"
  Delete "$INSTDIR\sqlite3.dll"
  Delete "$INSTDIR\unicodedata.pyd"
  Delete "$INSTDIR\VCRUNTIME140.dll"
  Delete "$INSTDIR\VCRUNTIME140_1.dll"

  Delete "$SMPROGRAMS\学生注册名单生成器\Uninstall.lnk"
  Delete "$SMPROGRAMS\学生注册名单生成器\Website.lnk"
  Delete "$DESKTOP\学生注册名单生成器.lnk"
  Delete "$SMPROGRAMS\学生注册名单生成器\学生注册名单生成器.lnk"

  RMDir "$SMPROGRAMS\学生注册名单生成器"

  RMDir /r "$INSTDIR\shiboken6"
  RMDir /r "$INSTDIR\pytz"
  RMDir /r "$INSTDIR\PySide6"
  RMDir /r "$INSTDIR\platforms"
  RMDir /r "$INSTDIR\pandas"
  RMDir /r "$INSTDIR\numpy"
  RMDir /r "$INSTDIR\Include"

  RMDir "$INSTDIR"

  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd

#-- 根据 NSIS 脚本编辑规则，所有 Function 区段必须放置在 Section 区段之后编写，以避免安装程序出现未可预知的问题。--#

Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "你确实要完全移除 $(^Name) ，及其所有的组件？" IDYES +2
  Abort
FunctionEnd

Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) 已成功地从你的计算机移除。"
FunctionEnd
