# Naik's Audiobook Downloader

A modern desktop application wrapper for downloading audiobooks from various online sources without needing to use the command line! This project provides an easy-to-use graphical interface with automatic browser cookie importing.

If you are interested, please contact me on: poornanandnaik24@gmail.com

## Features

- **Modern Interface**: Clean, dark-mode native desktop UI.
- **Easy Authentication**:
  - Securely log in to any site using the built-in Embedded Browser. Once you close the browser, your cookies are automatically captured for downloading.
  - Or manually load your own `cookies.txt` file.
  - Basic Username and Password login support for specific services.
- **Live Output**: Real-time console streaming so you can monitor your download progress directly in the app.
- **Supported Sites Viewer**: Built-in viewer to quickly check which platforms are supported and what authentication they require.

## Download for Windows

You can download the Windows installer from the repository:
1. Download [Audiobook-dl-Installer.exe](dist/Audiobook-dl-Installer.exe)
2. Double-click to run the setup. It will install the application and automatically create a desktop shortcut for you!

## How to Use

1. **Enter the Audiobook URL**: Paste the link to the audiobook you want to download in the URL field.
2. **Choose Output Location**: Click "Browse" to select the folder where the audiobook should be saved.
3. **Authenticate (If Required)**: 
   - **Automatic (Recommended)**: Click **"Login via Embedded Browser"**, sign into your account on the webpage, and then close the browser window. The app will automatically capture your secure login session!
   - **Manual**: Alternatively, you can enter your basic credentials in the Username/Password fields or use a custom `cookies.txt` file.
4. **Download**: Click the **Download** button and watch the live progress in the console log!

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
