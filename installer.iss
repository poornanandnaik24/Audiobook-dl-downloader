[Setup]
AppName=Naik's Audiobook Downloader
AppVersion=1.0
DefaultDirName={autopf}\Audiobook-dl
DefaultGroupName=Naik's Audiobook Downloader
OutputDir=dist
OutputBaseFilename=Audiobook-dl-Installer
Compression=lzma
SolidCompression=yes
SetupIconFile=icon.ico
UninstallDisplayIcon={app}\Audiobook-dl.exe
PrivilegesRequired=lowest

[Files]
Source: "dist\Audiobook-dl\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "icon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Naik's Audiobook Downloader"; Filename: "{app}\Audiobook-dl.exe"; IconFilename: "{app}\icon.ico"
Name: "{autodesktop}\Naik's Audiobook Downloader"; Filename: "{app}\Audiobook-dl.exe"; IconFilename: "{app}\icon.ico"
