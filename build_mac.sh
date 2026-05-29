#!/bin/bash
# Script to build the macOS application

echo "Installing requirements..."
pip3 install -r requirements-gui.txt
pip3 install .

echo "Building audiobook-dl-gui.app..."
# On macOS, --windowed creates a .app bundle automatically
pyinstaller --noconfirm --onefile --windowed --name audiobook-dl-gui gui.py

echo "Build complete! You can find the app in the 'dist' folder."
