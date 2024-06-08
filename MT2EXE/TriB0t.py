import pyautogui
import time


def loork(): 
    pyautogui.press('4')

def attack():
    pyautogui.keyDown('space')
    time.sleep(20)
    
    
#def move():
    
    

def main():
    while True:
        loork()
        attack()
        time.sleep(20)
        #move()
        
        
        
if __name__ == "__main__":
    main()
        