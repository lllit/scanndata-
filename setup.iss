
[Setup]
AppName=ScannData
AppVersion=0.1
DefaultDirName={pf}\ScannData
DefaultGroupName=ScannData
OutputDir=.
OutputBaseFilename=ScannDataInstaller_v0.1

[Files]
Source: "build\windows\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "installers\Tesseract-OCR\installer_tesseract.exe"; DestDir: "{tmp}"; Flags: deleteafterinstall

[Run]
Filename: "{app}\scanndata.exe"; Description: "Abrir aplicación"; Flags: nowait postinstall skipifsilent
Filename: "{tmp}\installer_tesseract.exe"; Parameters: "/silent"; Flags: waituntilterminated