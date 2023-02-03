import pyautogui
from pynput import keyboard
from time import sleep


sleep(5)
def myAction(keyPressed):
  
    while pyautogui.click == False:
        pyautogui.click(468, 740)
        sleep(.25)
        pyautogui.click(637,801)
        sleep(.25)
        pyautogui.click(1140,939)
        sleep(.25)
        if keyPressed == keyboard.Key.s:
            return False
            

