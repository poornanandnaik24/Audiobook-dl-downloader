# Audiobook Downloader GUI

A modern desktop application wrapper for downloading audiobooks from various online sources without needing to use the command line! This project provides an easy-to-use graphical interface with automatic browser cookie importing.

## Features

- **Modern Interface**: Clean, dark-mode native desktop UI.
- **Easy Authentication**:
  - Automatically extract authentication cookies directly from Chrome or Firefox with one click.
  - Or manually load your own `cookies.txt` file.
  - Basic Username and Password login support for specific services.
- **Live Output**: Real-time console streaming so you can monitor your download progress directly in the app.
- **Supported Sites Viewer**: Built-in viewer to quickly check which platforms are supported and what authentication they require.

## Download for Windows

You can download the ready-to-use Windows application from the repository:
1. Download [Audiobook-dl-Windows.exe](dist/Audiobook-dl-Windows.exe)
2. Double-click to run! (No installation required)

## How to use
1. Paste the **URL** of the audiobook you want to download.
2. Select your output folder.
3. If the site requires a login, either enter your credentials or use the **Import Firefox / Import Chrome** buttons to automatically pull in your active sessions.
4. Click **Download**. 

## Building for Mac

The Python GUI code (`gui.py`) is fully cross-platform! If you are on macOS, you can easily build your own `.app` bundle:

1. Open your Mac Terminal.
2. Navigate to this downloaded repository folder.
3. Run the included build script:
   ```bash
   chmod +x build_mac.sh
   ./build_mac.sh
   ```
4. Once completed, your new `audiobook-dl-gui.app` will be located in the `dist/` folder.

## Supported Services
Currently supports downloading from the following sources (Check the "Supported Sites" button in the app for details):
- audiobooks.com
- Blinkist
- Chirp
- eReolen
- Everand (Scribd)
- Librivox
- Nextory
- Overdrive
- Podimo
- Saxo
- Storytel / Mofibo
- YourCloudLibrary

---
*This GUI is built on top of the original [audiobook-dl](https://github.com/jo1gi/audiobook-dl) CLI tool.*
