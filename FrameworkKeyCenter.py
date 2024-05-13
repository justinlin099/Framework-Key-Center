import tkinter as tk
from tkinter import ttk
import pywinstyles
import sv_ttk
import imageres
from tkinter import PhotoImage
from ctypes import windll
import webbrowser
import winreg
from tkinter import filedialog
import time

SCREEN_ROTATION_LOCATION = "C:\Program Files\FrameworkKeyCenter\components\ScreenRotate\ScreenRotate.exe"  
COPILOT_LOCATION = "C:\Program Files\FrameworkKeyCenter\components\copilot\copilot.exe" 
TASK_MANAGER_LOCATION = "C:\Windows\System32\Taskmgr.exe"
RICK_ROLL_LOCATION = "C:\Program Files\FrameworkKeyCenter\components\\NGGYU\\NGGYU.exe"
CLIPBOARD_CONTROL_LOCATION = "C:\Program Files\FrameworkKeyCenter\components\CopyandPaste\CopyandPaste.exe"
TRACKPAD_CONTROL_LOCATION = "C:\Program Files\FrameworkKeyCenter\components\TouchPadToggle\TouchPadToggle.exe"
VERSION='Version: 1.0.4'

current_opaque = 0

def donate():
    # Open the browser to the donate page
    webbrowser.open('https://www.buymeacoffee.com/5b32VpsEp5')
    
def webTest():
    # Open the browser to the custom link
    webbrowser.open(customWeblinkEntry.get())
    
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
        winreg.SetValueEx(key, 'CustomLink', 0, winreg.REG_SZ, customLinkEntry.get())
        winreg.SetValueEx(key, 'CustomWeblink', 0, winreg.REG_SZ, customWeblinkEntry.get())
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
            elif(dropDown.current() == 4):
                winreg.SetValueEx(key, 'ShellExecute', 0, winreg.REG_SZ, CLIPBOARD_CONTROL_LOCATION)
            elif(dropDown.current() == 6):
                winreg.SetValueEx(key, 'ShellExecute', 0, winreg.REG_SZ, customLinkEntry.get())
            elif(dropDown.current() == 7):
                winreg.SetValueEx(key, 'ShellExecute', 0, winreg.REG_SZ, customWeblinkEntry.get())
            elif(dropDown.current() == 5):
                winreg.SetValueEx(key, 'ShellExecute', 0, winreg.REG_SZ, TRACKPAD_CONTROL_LOCATION)
            
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
            elif(dropDown.current() == 4): 
                winreg.SetValueEx(key, 'ShellExecute', 0, winreg.REG_SZ, CLIPBOARD_CONTROL_LOCATION)
            elif(dropDown.current() == 6):
                winreg.SetValueEx(key, 'ShellExecute', 0, winreg.REG_SZ, customLinkEntry.get())
            elif(dropDown.current() == 7):
                winreg.SetValueEx(key, 'ShellExecute', 0, winreg.REG_SZ, customWeblinkEntry.get())
            elif(dropDown.current() == 5):
                winreg.SetValueEx(key, 'ShellExecute', 0, winreg.REG_SZ, TRACKPAD_CONTROL_LOCATION)
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
        #restoreEntry
        customLinkEntry.configure(state='normal')
        customLinkEntry.delete(0, 'end')
        customLinkEntry.insert(0, winreg.QueryValueEx(key, 'CustomLink')[0])
        customLinkEntry.configure(state='readonly')
        customWeblinkEntry.delete(0, 'end')
        customWeblinkEntry.insert(0, winreg.QueryValueEx(key, 'CustomWeblink')[0])
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
        winreg.SetValueEx(key, 'CustomLink', 0, winreg.REG_SZ, '')
        winreg.SetValueEx(key, 'CustomWeblink', 0, winreg.REG_SZ, '')
        winreg.SetValueEx(key, 'ClipboardMode', 0, winreg.REG_DWORD, 0)
        winreg.CloseKey(key)
        switch.state(['!selected'])
        dropDown.configure(state='disabled')
    
    if(switch.instate(['selected'])):
        dropDown.configure(state='readonly')
    else:
        dropDown.configure(state='disabled')
        
    selectDropDown(None)
    print('Settings initiated')
    
def selectDropDown(event):
    # Select the dropdown
    if dropDown.current() == 6:
        #display the custom link frame
        customLinkFrame.pack(side='top', fill='x', expand=True, padx=10, pady=10)
        customWeblinkFrame.pack_forget()
    elif dropDown.current() == 7:
        customWeblinkFrame.pack(side='top', fill='x', expand=True, padx=10, pady=10)
        customLinkFrame.pack_forget()
    else:
        customLinkFrame.pack_forget()
        customWeblinkFrame.pack_forget()
    
def browseFile():
    # open the file dialog to select the application
    file_path = filedialog.askopenfilename(parent=root, title='Select an application or files', filetypes=[('Applications', '*.exe'), ('All files', '*.*')])
    if file_path:
        customLinkEntry.configure(state='normal')
        customLinkEntry.delete(0, 'end')
        customLinkEntry.insert(0, file_path)
        customLinkEntry.configure(state='readonly')
        
def opaque_window():
    global current_opaque
    current_opaque += 0.05
    root.attributes('-alpha',current_opaque)
    if current_opaque <1:
        time.sleep(0.01)
        opaque_window()


windll.shcore.SetProcessDpiAwareness(1)

root = tk.Tk()


root.title('Framework Key Center')
root.geometry('800x550')
root.resizable(False, False)
root.attributes('-alpha',0)




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
dropDownFrame.pack(side='top', fill='x',expand=True, padx=10, pady=10)

dropDownLabel = ttk.Label(dropDownFrame, text='Select an action', font=('Segoe UI', 10))
dropDownLabel.pack(side='left', padx=10)

dropDown = ttk.Combobox(dropDownFrame, values=['Screen Rotation', 'Copilot Key', 'TaskManager', 'RickRoll', 'Copy and Paste (Clipboard Control)', 'Enable/Disable TrackPad', 'Custom Application', 'Custom Link'], state='readonly')
dropDown.pack(side='right', fill='x', expand=True, padx=10)
dropDown.current(0)
dropDown.bind('<<ComboboxSelected>>', selectDropDown)

customLinkFrame = ttk.Frame(innerFrame)
customLinkFrame.pack(side='top', fill='x', expand=True, padx=10, pady=10)
customLinkFrame.pack_forget()

# customLinkLabel = ttk.Label(customLinkFrame, text='Custom link/application', font=('Segoe UI', 10))
# customLinkLabel.pack(side='left', padx=10)

customLinkEntry = ttk.Entry(customLinkFrame, state='readonly')
customLinkEntry.pack(side='left', fill='x', expand=True, padx=10)

customLinkBrowseButton = ttk.Button(customLinkFrame, text='Browse', command=browseFile)
customLinkBrowseButton.pack(side='right', padx=10)

customWeblinkFrame = ttk.Frame(innerFrame)
customWeblinkFrame.pack(side='top', fill='x', expand=True, padx=10, pady=10)
customWeblinkFrame.pack_forget()

customWeblinkEntry = ttk.Entry(customWeblinkFrame)
customWeblinkEntry.pack(side='left', fill='x', expand=True, padx=10)

customWeblinkTestButton = ttk.Button(customWeblinkFrame, text='Test', command=webTest)
customWeblinkTestButton.pack(side='right', padx=10)



bottomLabelFrame = ttk.Frame(innerFrame)
bottomLabelFrame.pack(side='bottom', fill='x', padx=10, pady=10)

versionLabel = ttk.Label(bottomLabelFrame, text=VERSION, font=('Segoe UI', 10))
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

root.after(1500, opaque_window)

sv_ttk.set_theme('dark')



pywinstyles.apply_style(root, 'acrylic')

initiate()

root.mainloop()