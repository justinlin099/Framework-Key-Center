import pyautogui
from pyautogui import hotkey as hk
from subprocess import Popen
pyautogui.FAILSAFE = False

hk('win','ctrl','d')

Popen("start msedge --new-window https://youtu.be/dQw4w9WgXcQ?si=iJOK42DV2AhJdGh8", shell=True)

from time import sleep
sleep(3)

hk('space')