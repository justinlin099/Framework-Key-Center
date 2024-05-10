import pyautogui
from pyautogui import hotkey as hk

pyautogui.FAILSAFE = False

with open("C:\Program Files\FrameworkKeyCenter\components\CopyandPaste\ClipboardState.cfg", 'r') as file:
    global state
    state = file.read()
    
with open("C:\Program Files\FrameworkKeyCenter\components\CopyandPaste\ClipboardState.cfg", 'w') as file:
    if(state == 'True'):
        hk('ctrl','c')
        file.write('False')
    else:
        hk('ctrl','v')
        file.write('True')
        
import tkinter as tk
import win32gui
import pywinstyles
from tkinter import ttk
import sv_ttk
from ctypes import windll
import imageres

# 取得當前前景窗口的 handle
current_window = win32gui.GetForegroundWindow()

def check_caps_lock():
    if(state == 'True'):
        label.config(image=copy)
        label.config(text="  Copied")
    else:
        label.config(image=paste)
        label.config(text="  Pasted")

    # 將焦點返回到當前前景窗口
    win32gui.SetForegroundWindow(current_window)

def close_window():
    root.destroy()
    
def opaque_window():
    root.attributes('-alpha',1)
    
windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()
root.overrideredirect(True)
root.attributes("-topmost", True)
root.attributes('-alpha',0)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
geomeryStr="200x80+"+str(int((screen_width-200)/2))+"+"+str(int(screen_height*0.85))
root.geometry(geomeryStr)

# labelFrame = ttk.Frame(root)
# labelFrame.pack(expand=True, fill='both', padx=20, pady=10)
paste = tk.PhotoImage(data=imageres.paste)
paste = paste.subsample(15)
copy = tk.PhotoImage(data=imageres.copy)
copy = copy.subsample(15)
# imageLabel = ttk.Label(labelFrame, image=copy)
# imageLabel.pack(side='left', padx=10,expand=True, fill='both')
# label = ttk.Label(labelFrame, text="", font=('Segoe UI', 12))
# label.pack(side='left', padx=10,expand=True, fill='both')

label = ttk.Button(root, text="", command=close_window, compound='left')
check_caps_lock()

label.pack(expand=True, fill='both')

pywinstyles.apply_style(root, 'acrylic')
sv_ttk.set_theme('dark')




# 將焦點返回到原始的前景窗口
root.after(10, lambda: win32gui.SetForegroundWindow(current_window))

root.after(100, opaque_window)

# 一秒後關閉視窗
root.after(1000, close_window)

root.mainloop()



