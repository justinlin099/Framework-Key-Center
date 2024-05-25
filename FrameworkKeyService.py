import keyboard
import mouse

keyboard.on_press_key(109, lambda x: mouse.press('middle'),suppress=True) # F2
keyboard.on_release_key(109, lambda x: mouse.release('middle'),suppress=True) # F2

keyboard.wait()