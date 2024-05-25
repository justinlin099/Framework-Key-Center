!include MUI2.nsh

!define MUI_COMPONENTSPAGE_SMALLDESC ;No value
!define MUI_UI "C:\Program Files (x86)\NSIS\Contrib\UIs\modern.exe" ;Value
!define MUI_INSTFILESPAGE_COLORS "000000 FFFFFF" ;Two colors
!define MUI_BGCOLOR "333333"
!define MUI_TEXTCOLOR "FFFFFF"
!define MUI_ICON "icon.ico"
!define MUI_UNICON "icon.ico"
!define MUI_WELCOMEFINISHPAGE_BITMAP "nsis.bmp"
!define MUI_UNWELCOMEFINISHPAGE_BITMAP "nsis.bmp"

!define MUI_WELCOMEPAGE_TITLE "Welcome to the Framework Key Center Installer"

;!define MUI_WELCOMEPAGE_TITLE_3LINES "Welcome to the\nFramework Key Center Installer"


!define MUI_WELCOMEPAGE_TEXT "Remap your framework key to do something cool! $\r$\n$\r$\nDisclaimer: This software is provided as is. Use at your own risk. $\r$\n$\r$\nThis software is not developed by Framework Computer, Inc. in any way. $\r$\n$\r$\nMade by JustinLin099"

Name "Framework Key Center"

OutFile "FrameworkKeyCenterInstaller-v1.0.5.exe"

; Request application privileges for Windows Vista and higher
RequestExecutionLevel admin

; Build Unicode installer
Unicode True

; The default installation directory
InstallDir $PROGRAMFILES64\FrameworkKeyCenter

;Page components
;Page instfiles

!insertmacro MUI_PAGE_WELCOME
;MUI_PAGE_LICENSE textfile
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH


UninstPage uninstConfirm
UninstPage instfiles

!insertmacro MUI_LANGUAGE "English"

Section "Framework Key Center (required)"

  SectionIn RO
  
  ; Set output path to the installation directory.
  SetOutPath $INSTDIR
  
  ; Put file there
  ; copy dist/FrameworkKeyCenter to $INSTDIR
  File /r "dist\FrameworkKeyCenter\*"
  
  ; Create the components directory
  CreateDirectory "$INSTDIR\components"

  SetOutPath "$INSTDIR\components"


  File /r "dist\copilot"


  File /r "dist\NGGYU"

  
  File /r "dist\ScreenRotate"

  File /r "dist\CopyandPaste"

  File /r "dist\TouchpadToggle"

  File /r "dist\FrameworkKeyService"

  AccessControl::GrantOnFile "$INSTDIR\components" "(BU)" "FullAccess"

  ; Write the installation path into the registry
  WriteRegStr HKLM SOFTWARE\FrameworkKeyCenter "Install_Dir" "$INSTDIR"
  
  ; Write the uninstall keys for Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\FrameworkKeyCenter" "DisplayName" "Framework Key Center"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\FrameworkKeyCenter" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\FrameworkKeyCenter" "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\FrameworkKeyCenter" "NoRepair" 1
  WriteUninstaller "$INSTDIR\uninstall.exe"
  
SectionEnd

Section "Start Menu Shortcuts"

  CreateDirectory "$SMPROGRAMS\Framework Key Center"
  CreateShortcut "$SMPROGRAMS\Framework Key Center\Uninstall.lnk" "$INSTDIR\uninstall.exe"
  CreateShortcut "$SMPROGRAMS\Framework Key Center\Framework Key Center.lnk" "$INSTDIR\FrameworkKeyCenter.exe"

SectionEnd


;--------------------------------

; Uninstaller

Section "Uninstall"
  
  ; Remove registry keys
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\FrameworkKeyCenter"
  DeleteRegKey HKLM SOFTWARE\FrameworkKeyCenter

  ; Remove files and uninstaller
  Delete $INSTDIR\FrameworkKeyCenter.exe
  Delete $INSTDIR\uninstall.exe

  ; Remove shortcuts, if any
  Delete "$SMPROGRAMS\Framework Key Center\*.lnk"

  ; Remove directories
  RMDir "$SMPROGRAMS\Framework Key Center"
  RMDir /r /REBOOTOK "$INSTDIR"

SectionEnd



