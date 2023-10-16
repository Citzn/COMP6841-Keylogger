from pynput import keyboard


def printKeyPress(key):
        print(key)



if __name__ == '__main__':
        with keyboard.Listener(on_press=printKeyPress) as listener:
                listener.join()