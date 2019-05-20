
[Setup]
AppName=Carey Special
AppVersion=0.5
AppPublisher=Carey Code Custom
DefaultDirName=C:\Program Files (x86)\CareySpecial
DefaultGroupName=Carey Special
Compression=lzma2
SolidCompression=yes
OutputDir=userdocs:Inno Setup Output
OutputBaseFilename=CareySpecialSetup

[Files]
Source: "CareySpecial.exe"; DestDir: "{app}"
Source: "Installers\*"; DestDir: "{app}\Installers"; Flags: recursesubdirs
Source: "_bz2.pyd"; DestDir:"{app}"
Source: "_hashlib.pyd"; DestDir:"{app}"
Source: "_lzma.pyd"; DestDir:"{app}"
Source: "_socket.pyd"; DestDir:"{app}"
Source: "_ssl.pyd"; DestDir:"{app}"
Source: "base_library.zip"; DestDir:"{app}"
Source: "CareySpecial.exe.manifest"; DestDir:"{app}"
Source: "pyexpat.pyd"; DestDir:"{app}"
Source: "python36.dll"; DestDir:"{app}"
Source: "select.pyd"; DestDir:"{app}"
Source: "unicodedata.pyd"; DestDir:"{app}"
Source: "VCRUNTIME140.dll"; DestDir:"{app}"
Source: "README.txt"; DestDir: "{app}"; Flags: isreadme
Source: "C.ico"; DestDir: "{app}"

[Icons]
Name: "{group}\CareySpecial"; Filename: "{app}\CareySpecial.exe"; IconFilename:"{app}\C.ico"
Name: "{userdesktop}\CareySpecial"; Filename: "{app}\CareySpecial.exe"; IconFilename:"{app}\C.ico"
