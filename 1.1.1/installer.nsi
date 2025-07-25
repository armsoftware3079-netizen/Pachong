\
; Spider Tool v1.1.1 - NSIS Installer Script
!define PRODUCT_NAME "Spider Tool"
!define PRODUCT_VERSION "1.1.1"
!define PRODUCT_PUBLISHER "SpiderSoft"
!define PRODUCT_DIR_REGKEY "Software\SpiderTool"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"
!define PRODUCT_EXEC "spider.exe"

SetCompressor lzma

OutFile "SpiderTool_Setup_v1.1.1.exe"
InstallDir "$PROGRAMFILES\SpiderTool"
InstallDirRegKey HKLM "${PRODUCT_DIR_REGKEY}" ""

Page directory
Page instfiles

Section "Install"
  SetOutPath "$INSTDIR"
  File /r "dist\spider.exe"
  File "README.md"
  File "version_log.md"
  File "requirements.txt"
  File "spider.py"
  File "spider_ui.py"
  File "spider_ocr.py"

  CreateDirectory "$INSTDIR\output"
  WriteUninstaller "$INSTDIR\Uninstall.exe"
SectionEnd

Section "Uninstall"
  Delete "$INSTDIR\spider.exe"
  Delete "$INSTDIR\spider.py"
  Delete "$INSTDIR\spider_ui.py"
  Delete "$INSTDIR\spider_ocr.py"
  Delete "$INSTDIR\README.md"
  Delete "$INSTDIR\version_log.md"
  Delete "$INSTDIR\requirements.txt"
  RMDir /r "$INSTDIR\output"
  Delete "$INSTDIR\Uninstall.exe"
  RMDir "$INSTDIR"
SectionEnd
