import keyboard
from win32gui import GetWindowText, GetForegroundWindow
from colorama import Fore,init
from os import system as cmd
from time import sleep


init()
cmd("cls")
cmd("title ShadowHop CS:GO")

def main():
    print(f"[{Fore.BLUE}INFO{Fore.RESET}] Started ShadowHop.")

    while True:
        if not GetWindowText(GetForegroundWindow()).startswith("Counter-Strike: Global Offensive"):
            continue

        if keyboard.is_pressed("space"):
            keyboard.write('space')
            sleep(0.07) #time between jumps (afais this one works the best)
            continue

        sleep(0.02)

if __name__ == '__main__':
    main()
