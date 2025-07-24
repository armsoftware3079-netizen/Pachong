Outfile "spider_installer.exe"
InstallDir $PROGRAMFILES\PythonSpiderTool
RequestExecutionLevel admin

Section
  SetOutPath $INSTDIR
  File "I:\python≈¿≥Ê\dist\spider.exe"
  CreateShortCut $DESKTOP\PythonSpiderTool.lnk $INSTDIR\spider.exe
SectionEnd


