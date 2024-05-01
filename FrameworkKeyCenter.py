import tkinter as tk
from tkinter import ttk
import pywinstyles
import sv_ttk
import imageres
from tkinter import PhotoImage
from ctypes import windll
import webbrowser
import winreg

SCREEN_ROTATION_LOCATION = "C:\Program Files\FrameworkKeyCenter\components\ScreenRotate\ScreenRotate.exe"  
COPILOT_LOCATION = "C:\Program Files\FrameworkKeyCenter\components\copilot\copilot.exe" 
TASK_MANAGER_LOCATION = "C:\Windows\System32\Taskmgr.exe"
RICK_ROLL_LOCATION = "C:\Program Files\FrameworkKeyCenter\components\\NGGYU\\NGGYU.exe"

def donate():
    # Open the browser to the donate page
    webbrowser.open('https://www.buymeacoffee.com/5b32VpsEp5')
    
def save():
    # Save the settings
    apply()
    root.quit()
    

def apply():
    # Apply the settings
    if(switch.instate(['selected'])):
        print('Switch is on')
        print('Action: ' + dropDown.get())
        #write to registry
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'Software\\FrameworkKeyCenter', 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, 'Switch', 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(key, 'Action', 0, winreg.REG_DWORD, dropDown.current())
        key.Close()
        #HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\AppKey\16
        #CHECK IF THE KEY EXISTS
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\AppKey\\16', 0, winreg.KEY_WRITE)
            #IF THE KEY EXISTS, UPDATE THE VALUE
            #set the value according to the action
            if(dropDown.current() == 0):
                winreg.SetValueEx(key, 'ShellExecute', 0, winreg.REG_SZ, SCREEN_ROTATION_LOCATION)
            elif(dropDown.current() == 1):
                winreg.SetValueEx(key, 'ShellExecute', 0, winreg.REG_SZ, COPILOT_LOCATION)
            elif(dropDown.current() == 2):
                winreg.SetValueEx(key, 'ShellExecute', 0, winreg.REG_SZ, TASK_MANAGER_LOCATION)
            elif(dropDown.current() == 3):
                winreg.SetValueEx(key, 'ShellExecute', 0, winreg.REG_SZ, RICK_ROLL_LOCATION)
            winreg.CloseKey(key)
        except FileNotFoundError:
            key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\AppKey\\16')
            #set the value according to the action
            if(dropDown.current() == 0):
                winreg.SetValueEx(key, 'ShellExecute', 0, winreg.REG_SZ, SCREEN_ROTATION_LOCATION)
            elif(dropDown.current() == 1):
                winreg.SetValueEx(key, 'ShellExecute', 0, winreg.REG_SZ, COPILOT_LOCATION)
            elif(dropDown.current() == 2):
                winreg.SetValueEx(key, 'ShellExecute', 0, winreg.REG_SZ, TASK_MANAGER_LOCATION)
            elif(dropDown.current() == 3):
                winreg.SetValueEx(key, 'ShellExecute', 0, winreg.REG_SZ, RICK_ROLL_LOCATION)
            winreg.CloseKey(key)
    else:
        print('Switch is off')
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'Software\\FrameworkKeyCenter', 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, 'Switch', 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key, 'Action', 0, winreg.REG_DWORD, 0)
        key.Close()
        #CHECK IF THE KEY EXISTS
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\AppKey\\16', 0, winreg.KEY_WRITE)
            #IF THE KEY EXISTS, DELETE IT
            winreg.DeleteValue(key, 'ShellExecute')
            winreg.CloseKey(key)
        except FileNotFoundError:
            pass
    print('Settings applied')
    
def toggleSwitch():
    # Toggle the switch
    if(switch.instate(['selected'])):
        dropDown.configure(state='readonly')
    else:
        dropDown.configure(state='disabled')

 
def initiate():
    # Initiate the settings
    # Check if the registry key exists
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'Software\\FrameworkKeyCenter', 0, winreg.KEY_READ)
        switchState = winreg.QueryValueEx(key, 'Switch')
        action = winreg.QueryValueEx(key, 'Action')
        winreg.CloseKey(key)
        if(switchState[0] == 1):
            switch.state(['selected'])
            dropDown.configure(state='readonly')
            dropDown.current(action[0])
        else:
            switch.state(['!selected'])
            dropDown.configure(state='disabled')
    except FileNotFoundError:
        # If the key does not exist, create it
        key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, 'Software\\FrameworkKeyCenter')
        winreg.SetValueEx(key, 'Switch', 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(key, 'Action', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        switch.state(['!selected'])
        dropDown.configure(state='disabled')
    
    if(switch.instate(['selected'])):
        dropDown.configure(state='readonly')
    else:
        dropDown.configure(state='disabled')
    print('Settings initiated')


windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()


root.title('Framework Key Center')
root.geometry('800x500')
root.resizable(False, False)



iconPic = PhotoImage(data=imageres.icon)

root.iconphoto(True, iconPic)
root.iconphoto(False, iconPic)

mainFrame = ttk.Frame(root)
mainFrame.pack(side='top', fill='both', expand=True, padx=10, pady=10)

topFrame = ttk.Frame(mainFrame)
topFrame.pack(side='top', fill='x',ipadx=10, ipady=10)

emptyLabel = ttk.Label(topFrame, text='')
emptyLabel.grid(row=0, column=0)


topLabel = ttk.Label(topFrame, text='Framework Key Center', font=('Segoe UI', 20))
topLabel.grid(row=1, column=0, padx=20, sticky='sw')

topSubLabel = ttk.Label(topFrame, text='Remap your framework key to do something cool!', font=('Segoe UI', 10))
topSubLabel.grid(row=2, column=0, padx=20, sticky='sw')


# button = ttk.Button(root, text='Button', style='my.TButton', bootstyle='success')
# button.pack(ipadx=10, ipady=5, padx=10, pady=10)

innerFrame = ttk.Frame(mainFrame)
innerFrame.pack(side='top', fill='both', expand=True, padx=10, pady=10)

switchFrame = ttk.Frame(innerFrame)
switchFrame.pack(side='top', fill='x', padx=10, pady=10)

switchLabel = ttk.Label(switchFrame, text='Enable Framework key remap', font=('Segoe UI', 10))
switchLabel.pack(side='left')

switch = ttk.Checkbutton(switchFrame, style='Switch.TCheckbutton', command=toggleSwitch)
switch.pack(side='right')

dropDownFrame = ttk.Frame(innerFrame)
dropDownFrame.pack(side='top', fill='both',expand=True, padx=10, pady=10)

dropDownLabel = ttk.Label(dropDownFrame, text='Select an action', font=('Segoe UI', 10))
dropDownLabel.pack(side='left', padx=10)

dropDown = ttk.Combobox(dropDownFrame, values=['Screen Rotation', 'Copilot Key', 'TaskManager', 'RickRoll'], state='readonly')
dropDown.pack(side='right', fill='x', expand=True, padx=10)
dropDown.current(0)



bottomLabelFrame = ttk.Frame(innerFrame)
bottomLabelFrame.pack(side='bottom', fill='x', padx=10, pady=10)

versionLabel = ttk.Label(bottomLabelFrame, text='Version: 1.0.0', font=('Segoe UI', 10))
versionLabel.pack(side='left')

authorLabel = ttk.Label(bottomLabelFrame, text='Made by JustinLin099 with ❤️', font=('Segoe UI Emoji', 10))
authorLabel.pack(side='right')

bottomButtonFrame = ttk.Frame(innerFrame)
bottomButtonFrame.pack(side='bottom', fill='x', padx=10, pady=10)

okButton = ttk.Button(bottomButtonFrame, text='OK', command=save)
okButton.pack(side='right')

applyButton = ttk.Button(bottomButtonFrame, text='Apply', command=apply)
applyButton.pack(side='right', padx=10)

cancelButton = ttk.Button(bottomButtonFrame, text='Cancel', command=root.quit)
cancelButton.pack(side='right')

donateButton = ttk.Button(bottomButtonFrame, text='Donate', command=donate)
donateButton.pack(side='left')



sv_ttk.set_theme('dark')



pywinstyles.apply_style(root, 'acrylic')

initiate()

root.mainloop()