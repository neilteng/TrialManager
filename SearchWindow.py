from tinydb import TinyDB, Query
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from pprint import pprint
import SearchWindow, Modify, Delete, OpenDir
import os


def populate(frame, search_box, wd):
    db = TinyDB('./resources/db.json')

    modifyButton = tk.Button(frame, text="Modify", command = Modify)
    modifyButton.grid(row = 0, column = 0, padx=(150,10),pady=10)
    modifyButton.configure(font=("Times New Roman", 12, "bold"))


    deleteButton = tk.Button(frame, text="Delete", command = Delete)
    deleteButton.grid(row = 0, column = 1, padx=10,pady=10)
    deleteButton.configure(font=("Times New Roman", 12, "bold"))


    inputValue=search_box.get("1.0","end-1c")

    Trails = Query()

    # pprint(inputValue)
    def showResult(rowNum, result):
        tk.Button(frame, text="open", command = lambda: OpenDir.openTrialFolder(frame, os.path.join(wd+'/./' + result['file_dir']))).grid(row = rowNum, column = 0, pady=10)
        SearchResult = tk.Text(frame, width=40, height=1)
        SearchResult.insert('1.0', result['file_dir'])
        SearchResult.grid(row=rowNum, column=1, pady=10)
        SearchResult.configure(bg=frame.cget('bg'), relief="flat", font=("Times New Roman", 10, "bold"), state="disabled")

    rowNum = 1
    for result in db.search( eval(inputValue) ):
        # pprint(result)
        showResult(rowNum, result)
    
        rowNum+=1

def onFrameConfigure(canvas):
    '''Reset the scroll region to encompass the inner frame'''
    canvas.configure(scrollregion=canvas.bbox("all"))

def search(search_box, wd):
    editor = tk.Tk()
    editor.title('SearchTrails')
    editor.geometry("800x760")
    
    canvas = tk.Canvas(editor, borderwidth=0,) #background="#ffffff")
    frame = tk.Frame(canvas,)# background="#ffffff")
    vsb = tk.Scrollbar(editor, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)

    vsb.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.create_window((4,4), window=frame, anchor="nw")

    frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

    populate(frame, search_box, wd)