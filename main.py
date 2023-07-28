import os
import sys
import json
import tkinter
import urllib.request
import tkinter.simpledialog
import tkinter.messagebox
IP = 'localhost:2333'
try:
    firstOpen = urllib.request.urlopen('http://' + IP + '/api/v1/fristopen').read()
    firstOpen = json.loads(firstOpen)
    firstOpen = firstOpen['result']
    firstOpen = bool(firstOpen)
except:
    firstOpen = False
def openCommandPrompt() -> bool:
    kernel = sys.platform
    if kernel == 'win32':
        os.system('cmd /c start powershell')
    else:
        os.system('bash')
    return True

def saveFile(text) -> bool:
    saveTo = tkinter.simpledialog.askstring(title='File name',prompt='Please enter your file name')
    filename = tkinter.simpledialog.askstring(title='Save directory',prompt='Please enter your save directory')
    path = saveTo + filename
    try:
        with open(path,'w') as f:
            f.write(text)
        tkinter.messagebox.showinfo('Over','Succeed!')
        return True
    except:
        tkinter.messagebox.showerror('Error','Cannot open file.')
        return False
    
def showVersion() -> bool:
    tkinter.messagebox.showinfo('Version','Visual ASM - Better ASM IDE. By: Loong.\nGet help: https://dev.minecraftbox.link/asm/help')
    return True

window = tkinter.Tk()
window.title('Visual ASM 1.0')
window.geometry("850x400")

version = tkinter.Label(window,text='Visual ASM Version 1.0')
text = tkinter.Text(window, height=24)
save = tkinter.Button(window, text="Save", command=lambda : saveFile(text.get(1.0,'end')))
comd = tkinter.Button(window, text="Open Command Prompt", command=lambda : openCommandPrompt())
vers = tkinter.Button(window, text="Version", command=lambda : showVersion())

text.grid(column=0, row=0)
version.grid(column=1, row=1)
save.grid(row=3,column=3)
comd.grid(row=3,column=1)
vers.grid(row=3,column=2)
if firstOpen:
    tkinter.messagebox.showinfo('Tips','Welcome to Visual ASM!\nGet help: https://dev.minecraftbox.link/asm/help')
window.mainloop()
