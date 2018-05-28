import pyautogui
from pynput import keyboard
import time

#  ======== settings ========
delay = 1   # in seconds
message = 'Hello World!'
pause = True
running = True
#  ==========================

def on_press(key):
    global running, pause

    if key == keyboard.Key.f1:
        pause = False
        print("[Resumed]")
    elif key == keyboard.Key.f2:
        pause = True
        print("[Paused]")
    elif key == keyboard.Key.esc:
        running = False
        print("[Exit]")

def display_controls():
    print("// Settings: ")
    print("\t message = " + message)
    print("\t delay = " + str(delay) + '\n')
    print("// Controls:")
    print("\t F1 = Resume")
    print("\t F2 = Pause")
    print("\t F3 = Exit")
    print("-----------------------------")
    print('Press F1 to start ...')

def main():
    lis = keyboard.Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.typewrite(message)
            time.sleep(delay)

    lis.stop()

if __name__ == "__main__":
    main()