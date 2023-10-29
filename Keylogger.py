from pynput import keyboard
from win32 import win32clipboard
import pyperclip
import time
import threading

oldClipboard = ''

def printKeyPress(key):
    print(str(key))
    # with open("recording.txt", mode='a') as f:
        # f.write(str(key))
        # f.write('\n')
        # f.close()

def shortcutsPressed():
    with open("recording.txt", mode='a') as f:
        global oldClipboard

        # win32clipboard.OpenClipboard()
        # data = str(win32clipboard.GetClipboardData())
        # win32clipboard.CloseClipboard()

        data = pyperclip.paste()

        print("asdadsad: {a}".format(a = data))
        print("asdadsad: {a}".format(a = oldClipboard))
        print(data == oldClipboard)
        while (data == oldClipboard):
            # win32clipboard.OpenClipboard()
            # data = str(win32clipboard.GetClipboardData())
            # win32clipboard.CloseClipboard()

            data = pyperclip.paste()

            oldClipboard == data

        print(data)
        print(oldClipboard)

def readKeyboardInput():
    global oldClipboard
    with keyboard.Listener(on_press=printKeyPress) as listener:
        listener.join()

def readClipboard():
    global oldClipboard
    with keyboard.GlobalHotKeys({'<ctrl>+c' : shortcutsPressed}) as h:
        h.join()
    # hotkey = keyboard.HotKey(keyboard.HotKey.parse('<ctrl>+c'), shortcutsPressed)
    

threading.Thread(target = readKeyboardInput, name ='keyboardReader', daemon= False).start()
threading.Thread(target = readClipboard, name = 'clipboardReader', daemon= True).start()


