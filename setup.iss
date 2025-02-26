
[Setup]
AppName=ExtData
AppVersion=0.1
DefaultDirName={pf}\ExtData
DefaultGroupName=ExtData
OutputDir=.
OutputBaseFilename=ExtDataInstaller

[Files]
Source: "build\windows\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "installers\Tesseract-OCR\installer_tesseract.exe"; DestDir: "{tmp}"; Flags: deleteafterinstall

[Run]
Filename: "{app}\ext_data.exe"; Description: "Abrir aplicación"; Flags: nowait postinstall skipifsilent
Filename: "{tmp}\installer_tesseract.exe"; Parameters: "/silent"; Flags: waituntilterminated