#!/bin/bash
# Script to build the macOS application

echo "Installing requirements..."
pip3 install -r requirements-gui.txt
pip3 install .

echo "Building audiobook-dl-gui.app..."
# On macOS, --windowed creates a .app bundle automatically
pyinstaller --noconfirm --windowed --name audiobook-dl-gui --collect-all audiobookdl --exclude-module PySide6 --exclude-module matplotlib --exclude-module IPython --exclude-module sphinx --exclude-module pytest gui.py

echo "Build complete! You can find the app in the 'dist' folder."
