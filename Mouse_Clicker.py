import pyautogui
import random
from pynput import keyboard
from time import sleep

shouldStop = False
def on_press(key):
    global shouldStop
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        if key.char == 's':
            shouldStop = True
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

def myAction():
    global shouldStop
    sleep(3)
    while not shouldStop:
        x1 = random.randrange(419, 515)
        y1 = random.randrange(893, 989)
        x2 = random.randrange(522, 963)
        y2 = random.randrange(975, 1028)
        x3 = random.randrange(1021, 1205)
        y3 = random.randrange(917, 959)
        pyautogui.leftClick(x1, y1)
        pyautogui.leftClick(x1, y1)
        sleep(.25)
        pyautogui.leftClick(x2, y2)
        sleep(.25)
        pyautogui.leftClick(x3, y3)
        sleep(.25)
        
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
myAction()    
listener.stop()