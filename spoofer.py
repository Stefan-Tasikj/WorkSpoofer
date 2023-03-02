import pyautogui
import time
import random
from pynput import keyboard
#Open tabs on your browser, start the script, switch to the browser window, after 10 seconds it will simulate movement
#and keep switching tabs and scrolling and moving the mouse randomly within the browser. Press end to stop.
pyautogui.FAILSAFE = 0
# Set the duration of the mouse movements in seconds
MOUSE_MOVE_DURATION = 0.8
pyautogui.moveTo(0, 0)
break_program = False
time.sleep(10)

#Terminate the program if the end key is pressed
def on_press(key):
    global break_program
    if key == keyboard.Key.end:
        print('end pressed')
        break_program = True
        return False


with keyboard.Listener(on_press=on_press) as listener:
    while not break_program:
        # Randomly select a number of tabs to switch
        num_tabs = random.randint(1, 8)

        # Press Ctrl+Tab num_tabs times to switch between tabs
        for i in range(num_tabs):
            pyautogui.hotkey('ctrl', 'tab')

        time.sleep(random.uniform(1, 10))
        pyautogui.scroll(clicks=random.randint(-500, 500))
        for x in range(4):
            pyautogui.hotkey('ctrl')

        # Randomly move the mouse to a new location on the screen
        x = random.randint(100, pyautogui.size().width)
        y = random.randint(100, pyautogui.size().height)
        pyautogui.moveTo(x, y, duration=MOUSE_MOVE_DURATION, tween=pyautogui.easeInOutQuad)
    listener.join()
