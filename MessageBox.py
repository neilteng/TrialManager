from tkinter import messagebox 

def AskNewOrUsedDate():
    return messagebox.askquestion(title="New Experiment Date or not?", message="Do you wish to create a new date or continue on the last experiment date?")
