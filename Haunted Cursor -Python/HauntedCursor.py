import pyautogui
import time

def main():
    while True:
        pyautogui.moveRel(20, 20)
        time.sleep(3)

if __name__ == '__main__':
    main()
