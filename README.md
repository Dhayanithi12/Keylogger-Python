# Keylogger-Python

This Python script implements a basic keylogger for the Windows operating system using the Windows API (ctypes). The keylogger captures key presses and logs them into a file (windows.txt) while also setting persistence via a registry entry to run on system startup.

## Features
Captures key presses and logs them into windows.txt.
Handles special keys like Caps Lock, Num Lock, Shift keys, and more.
Sets persistence by adding a registry entry under HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run.
Runs continuously in the background, starting automatically on system startup.
Requirements
Python 3.x (tested with Python 3.6+)
Windows operating system (tested on Windows 10)
Usage
Clone the repository:

## bash
Copy code
git clone https://github.com/Dhayanithi12/ Keylogger-Python.git
cd python-keylogger
Install dependencies (no additional libraries required):

This script uses only standard Python libraries.

## Run the keylogger:

Execute the script with Python:

bash
Copy code
python keylogger.py
The keylogger will start running in the background. Press Ctrl+C to stop it.

Retrieve logs:

Logs are stored in windows.txt in the same directory where the script is executed.

Notes
Persistence: The script attempts to set persistence by adding a registry entry under HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run. This allows the keylogger to start automatically on system startup.

Security: This script is for educational purposes only. Ensure you have appropriate permissions before running it on any system.

Antivirus Software: Some antivirus programs may detect keyloggers as malicious software. Use responsibly and avoid using on systems where you do not have permission.

License
This project is licensed under the MIT License - see the LICENSE file for details.

