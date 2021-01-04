import tkinter as tk
from tkinter.scrolledtext import ScrolledText
# import pymongo as pmg,
import SearchWindow, MessageBox, NewTrailWindow, CtrlKeys, GetWorkingDir, UpdateDir
from pprint import pprint
import ctypes

root = tk.Tk()

# mongoClient = pmg.MongoClient()

# db = mongoClient["TrailManager"]
# collection = db['Trails']

root.title('Trial Manager -- manage your experiments easier')
root.geometry("1080x860")


# Work Directory
wdLabel = tk.Label(root, text = "Please specify full working directory. Default is following directory.")
wdLabel.grid(row=0,column=0)
wdLabel.configure(font=("Times New Roman", 20, "bold"))

dirEntry = tk.Entry(root, width = 60,  font="TimesNewRoman 18")
dirEntry.grid(row = 1, column = 0, padx=(20,20), pady=(20,20), ipady=10)
dirEntry.insert(0, GetWorkingDir.workingDir())

wd = dirEntry.get()
def comfirmDir():
    wd = dirEntry.get()
    UpdateDir.updateDir(wd)
    
DirButton = tk.Button(root, text="comfirm", command = comfirmDir )
DirButton.grid(row = 1, column = 1)
DirButton.configure(font=("Times New Roman", 18, "bold"))


# New Trail
def questionWrapper():
    response = MessageBox.AskNewOrUsedDate()
    if response == 'yes':
        isNewDate = True
    else:
        isNewDate = False

    NewTrailWindow.NewTrailWindow(isNewDate, wd)

newTrailButton = tk.Button(root, text="New Trail", command =  questionWrapper, bg='#0052cc', fg='#ffffff')
newTrailButton.grid(row=2, column=0, columnspan = 3, pady=20 )
newTrailButton.configure(font=("Times New Roman", 18, "bold"))

# Search
search_box = ScrolledText(root, width=80, height=20, undo=True, autoseparators=True, maxundo=-1)
search_box.grid(row = 3, column = 0, pady=(10,3), padx=40, columnspan =2)
search_box.configure(font=("Times New Roman", 18, "bold"))
search_box.bind("<Control-KeyPress>", CtrlKeys.ctrlKeys)
search_box.insert('1.0', "( (Trails.setup.Ca > 10) | (Trails.setup.Na > 10) ) & ( (Trails.setup.Na >= 100) | (Trails.setup.fps == 10) )")


searchButton = tk.Button(root, text="Search", command = lambda: SearchWindow.search(search_box, wd))
searchButton.grid(row=4, column=0,  pady=10, padx=10, columnspan =2)
searchButton.configure(font=("Times New Roman", 18, "bold"))

ctypes.windll.shcore.SetProcessDpiAwareness(1)

root.tk.call('tk', 'scaling', 2.0)

root.mainloop()
