import pyautogui as pt
from time import sleep

def nav_to_image(image, clicks, off_x=0, off_y = 0):
    position = pt.locateCenterOnScreen(image, confidence=.7)
    if position is None:
        print(f"{image} not found")
        return 0
    else:
        pt.moveTo(position, duration=.1)
        pt.moveRel(off_x, off_y, duration=.1)
        pt.click(clicks=clicks, interval=.3)
        
        
# Moves the character
# x = attack
# c = place

def move_character(key_press, duration, action='walking'):
    pt.keyDown(key_press)
    
    if action == 'walking':
        print('Walking')
    elif action == 'attack':
        pt.keyDown('x')
        
    sleep(duration)
    pt.keyUp('x')
    pt.keyUp(key_press)
    

def locate_lava():
    position = pt.locateCenterOnScreen("../data/images/lava.png", confidence=.5)
    if position is None:
        return False
    else:
        move_character('s', 2)
        print('Found lava')
        return True
    
sleep(3)
nav_to_image("../data/images/start_game.png", 3)
duration = 10
while duration != 0:
    if not locate_lava():
        move_character('w', 2, 'attack')
    else:
        break
    
    duration -= 1
    print(f'Time remaining = {duration}')
