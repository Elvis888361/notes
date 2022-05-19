import tkinter as tk
from tkinter import *
from tkinter import messagebox,filedialog
import os

def createWidgets():
    global textArea
    textArea=Text(root)
    textArea.grid(sticky=N+E+S+W)

    menuBar=Menu(root)
    root.config(menu=menuBar)
    fileMenu=Menu(menuBar,tearoff=0)
    fileMenu.add_command(label="New",command=newFile)
    fileMenu.add_command(label="open",command=openFile)
    fileMenu.add_command(label="save",command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit",command=exit)
    menuBar.add_cascade(label="File",menu=fileMenu)

    editMenu=Menu(menuBar,tearoff=0)
    editMenu.add_command(label="cut",command=cut)
    editMenu.add_command(label="copy",command=copy)
    editMenu.add_command(label="paste",command=paste)
    menuBar.add_cascade(label="Edit",menu=editMenu)

    helpMenu=Menu(menuBar,tearoff=0)
    helpMenu.add_command(label="About Notepad",command=help)
    menuBar.add_cascade(label="Help",menu=helpMenu)
def newFile():
    global textArea
    root.title("untitled - Notepad")
    file = None
    textArea.delete(1.0,END)
def openFile():
    global textArea
    file=filedialog.askopenfile(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Document","*.txt")])
    file=file.name
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + " -Notepad")
        textArea.delete(1.0,END)
        file=open(file,"rb")
        textArea.insert(1.0,file.read())
        file.close()
def saveFile():
    global textArea,file
    if file ==None:
        file=filedialog.asksaveasfilename(initialfile="untitled.txt",defaultextension=".txt",filetypes=[("All files","*.*"),("Text Document","*.txt")])
        if file==None:
            file=None
        else:
            file=open(file,"w")
            file.write(textArea.get(1.0,END))
            file.close()
            file=file.name
            root.title(os.path.basename(file)+"-Notepad")
    else:
        file=open(file,"w")
        file.write(textArea.get(1.0,END))
        file.close()
def exit():
    root.destroy()
def cut():
    global textArea
    textArea.event_generate("<<Cut>>")
def copy():
    global textArea
    textArea.event_generate("<<Copy>>")
def paste():
    global textArea
    textArea.event_generate("<<Paste>>")
def help():
    messagebox.showinfo("Notepad","This simple notepad is developed by Elvis")




root=tk.Tk()
root.title("untitled - Notepad")
file=None
createWidgets()
root.mainloop()