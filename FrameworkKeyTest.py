import keyboard
import mouse

while True:
      print(keyboard.read_hotkey(suppress=True))
 
keyboard.wait()   