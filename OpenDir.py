from tkinter import filedialog
import os
def openTrialFolder(parent, dir):
    # print(dir)
    filename = filedialog.askopenfilename(parent = parent, initialdir = dir, title="select file")
    os.system(filename)