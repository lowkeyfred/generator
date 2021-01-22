; �ýű�ʹ�� HM VNISEdit �ű��༭���򵼲���

; ��װ�����ʼ���峣��
!define PRODUCT_NAME "ѧ��ע������������"
!define PRODUCT_VERSION "1.2"
!define PRODUCT_PUBLISHER "SCUPI"
!define PRODUCT_WEB_SITE "https://support.scupi.cn"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\Generator.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"

SetCompressor lzma

; ------ MUI �ִ����涨�� (1.67 �汾���ϼ���) ------
!include "MUI.nsh"

; MUI Ԥ���峣��
!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"

; ��ӭҳ��
!insertmacro MUI_PAGE_WELCOME
; ���Э��ҳ��
!insertmacro MUI_PAGE_LICENSE "License.txt"
; ��װĿ¼ѡ��ҳ��
!insertmacro MUI_PAGE_DIRECTORY
; ��װ����ҳ��
!insertmacro MUI_PAGE_INSTFILES
; ��װ���ҳ��
!define MUI_FINISHPAGE_RUN "$INSTDIR\Generator.exe"
!insertmacro MUI_PAGE_FINISH

; ��װж�ع���ҳ��
!insertmacro MUI_UNPAGE_INSTFILES

; ��װ�����������������
!insertmacro MUI_LANGUAGE "SimpChinese"

; ��װԤ�ͷ��ļ�
!insertmacro MUI_RESERVEFILE_INSTALLOPTIONS
; ------ MUI �ִ����涨����� ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "Setup.exe"
InstallDir "$PROGRAMFILES\ѧ��ע������������"
InstallDirRegKey HKLM "${PRODUCT_UNINST_KEY}" "UninstallString"
ShowInstDetails show
ShowUnInstDetails show
BrandingText "ѧ��ע������������"

Section "MainSection" SEC01
  SetOutPath "$INSTDIR"
  SetOverwrite ifnewer
  File /r "dist\Generator\*.*"
  CreateDirectory "$SMPROGRAMS\ѧ��ע������������"
  CreateShortCut "$SMPROGRAMS\ѧ��ע������������\ѧ��ע������������.lnk" "$INSTDIR\Generator.exe"
  CreateShortCut "$DESKTOP\ѧ��ע������������.lnk" "$INSTDIR\Generator.exe"
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
  CreateShortCut "$SMPROGRAMS\ѧ��ע������������\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\ѧ��ע������������\Uninstall.lnk" "$INSTDIR\uninst.exe"
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
 *  �����ǰ�װ�����ж�ز���  *
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

  Delete "$SMPROGRAMS\ѧ��ע������������\Uninstall.lnk"
  Delete "$SMPROGRAMS\ѧ��ע������������\Website.lnk"
  Delete "$DESKTOP\ѧ��ע������������.lnk"
  Delete "$SMPROGRAMS\ѧ��ע������������\ѧ��ע������������.lnk"

  RMDir "$SMPROGRAMS\ѧ��ע������������"

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

#-- ���� NSIS �ű��༭�������� Function ���α�������� Section ����֮���д���Ա��ⰲװ�������δ��Ԥ֪�����⡣--#

Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "��ȷʵҪ��ȫ�Ƴ� $(^Name) ���������е������" IDYES +2
  Abort
FunctionEnd

Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) �ѳɹ��ش���ļ�����Ƴ���"
FunctionEnd
