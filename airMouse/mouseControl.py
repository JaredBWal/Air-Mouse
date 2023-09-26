import pyautogui


def moveTo(x, y):
    if(x > 50 or y > 50):
        pyautogui.moveTo(x, y, duration=0)

def clickMouse(x,y):
    #print("Clicking")

    pyautogui.click()

