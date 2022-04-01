import tkinter as tk
from mathParser import mathParser
import keyboard
import os
#!/usr/bin/env python3
#Author: @AuthoredEntropy 
import tkinter.ttk as ttk
import json
def returnConfig():
    with open('./config.json') as f:
        data = json.load(f)
        return data
workingDir = os.getcwd()
config = returnConfig()
defaultPath= config["defaultPath"]
darkBgClr= config["darkBgClr"]
bgClr=config["bgClr"]
PBHClr = config["PHBClr"]
offClr = config["offClr"]
highlightClr=config["highlightClr"]
higherLightClr=config["higherLightClr"]
def addTab(master):
    MonsterFrame = tk.Frame(master,width=1270,height=780, bg =bgClr)
    MonsterFrame.pack()
    MonsterFrame.pack_propagate(0)
    return MonsterFrame
def addHorizontalSpacer(master, w, side="left", color =bgClr):
    spacer = tk.LabelFrame(master=master, width=w, bg =color, relief="flat")
    spacer.pack(side=side, fill="both")
    return spacer
from tkinter.filedialog import asksaveasfile
from tkinter import filedialog as fd 
def selectFolder(defaultPath):
    folder_selected = fd.askdirectory(initialdir =defaultPath)
    return folder_selected
def selectFile(defaultPath):
    try:
        file = fd.askopenfile(initialdir =defaultPath)
        return file.read()
    except AttributeError as e:
        #if file dialog was closed
        return 0
def selectFiles(defaultPath):
    try:
        files = fd.askopenfiles(initialdir =defaultPath)
        return files
    except AttributeError as e:
        #if file dialog was closed
        return 0
def saveFile(data,initDir,initName="unnamed"):
    try:
        files =[('default data type', '*.json*')]
        file = asksaveasfile(filetypes=files,defaultextension=".json",initialdir=initDir,initialfile=initName)
        file.write(data)
    except AttributeError as e:
        #if file dialog was closed
        pass
def addVerticalSpacer(master, h, side="top", color =bgClr):
    spacer = tk.LabelFrame(master=master, height=h, bg =color,relief="flat")
    spacer.pack(fill="both",side=side)
    return spacer
def addLabel(master, name,text,padding=0,side="top"):
    exec(f"{name} = tk.Label(master, text=text)")
    exec(f"{name}.pack(side=\"{side}\", anchor=\"w\", padx={padding})")
    return locals()[f"{name}"]
def editPrompt(root,existingText):
    top = createTopLevel()
    top.overrideredirect(1)
    x = root.winfo_x()
    y = root.winfo_y()
    h = root.winfo_height()
    w = root.winfo_width()
    top.geometry("%dx%d+%d+%d" % (300, 20, x + (w/4.5), y + 80))
    label = tk.Label(top, text="enter new title:")
    text = addInput(top)
    text.insert(0,existingText)
    label.pack(side="left")
    text.pack(side="left")
    text.focus()
    return {"text":text,"top":top}
def addInput(master,enableMStrings=True,width=200,padding=5,alwaysParse=False):
    addVerticalSpacer(master,1, "top", bgClr)
    ContainerFrame = tk.Frame(master, background = 'grey', borderwidth = 1, relief = "sunken")
    ContainerFrame.pack(side="top",padx=padding)
    ent = tk.Entry(ContainerFrame, width=width)
    ent.pack(side="top")
    x = mathParser()
    if(enableMStrings==True):
        def parse(entry):
            string = entry.get()
            if("!m" in string):
                        x = mathParser()
                        text=x.parseString(string)
                        entry.delete(0, tk.END)
                        entry.insert(0, text)
        ent.bind("<Return>",lambda x:parse(ent))
    elif(alwaysParse==True):
        def parse(entry):
            text=x.parseString(entry.get())
            entry.delete(0, tk.END)
            entry.insert(0, text)
        ent.bind("<Return>",lambda x:parse(ent))

    return ent
def createTopLevel():
    top = tk.Toplevel()
    top.bind("<Key>",lambda event: keyCombos(event,top))
    return top
def addDropDown(master,name,options, size=50,side="top",padding=5):
    Variable = tk.StringVar()
    Variable.set(options[0])
    dropdownMenu = ttk.Combobox(master, width=size,textvariable= Variable)
    dropdownMenu['values'] = options
    x = mathParser()
    def parse(variable):
        text=x.parseString(variable.get())
        Variable.set(text)
    dropdownMenu.bind("<Return>",lambda x:parse(Variable))
    dropdownMenu.pack(padx=padding,side=side)
    return dropdownMenu
def addSpinbox(master,min,max,inc,width,side="top",anchor="w",padding=5):
    spinBox = ttk.Spinbox(master,from_=min,to=max,increment=inc,width=width)
    spinBox.pack(side=side,anchor=anchor,padx=padding)
    x = mathParser()
    def parse(spinBox):
        text=x.parseString(spinBox.get())
        spinBox.set(text)
    spinBox.bind("<Return>",lambda x:parse(spinBox))
    return spinBox
def keyCombos(event,root):
    try:
        if event.char == event.keysym:
                key = event.char
        else:
            key = event.keysym
        if(keyboard.is_pressed("ctrl")):
            if(key=="space"):
                focused=root.focus_get() 
                text =focused.get()
                focused.delete(0, tk.END)
                focused.insert(tk.END, text+"!m1d20")
            elif(key=="m"):
                focused=root.focus_get() 
                text =focused.get()
                focused.delete(0, tk.END)
                focused.insert(tk.END, text+"!m")
    except AttributeError:
        pass
    