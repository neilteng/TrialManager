import os.path
from os import path
from tkinter import messagebox
from UpdateDir import updateDir

def workingDir():
    dir = None
    if(path.exists('resources/workingDirectory.txt')):
        with open('resources/workingDirectory.txt','r') as file:
            dir = file.readline()
            if(len(dir)==0):
                updateDir()
    else:
        updateDir()

        # messagebox.showwarning(title="Input is not Valid", message="Input Directory is not valid. Using current directory as Defalut\nOr lpease type in a valid directory.")

    return dir