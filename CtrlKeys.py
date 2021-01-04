import ctypes
#https://stackoverflow.com/questions/40946919/python-tkinter-copy-paste-not-working-with-other-languages
def is_ru_lang_keyboard():
    u = ctypes.windll.LoadLibrary("user32.dll")
    pf = getattr(u, "GetKeyboardLayout")
    return hex(pf(0)) == '0x4190419'

def ctrlKeys(event):
    if is_ru_lang_keyboard():
        if event.keycode==86:
            event.widget.event_generate("<<Paste>>")
        if event.keycode==67: 
            event.widget.event_generate("<<Copy>>")    
        if event.keycode==88: 
            event.widget.event_generate("<<Cut>>")    
        if event.keycode==65535: 
            event.widget.event_generate("<<Clear>>")
        if event.keycode==65: 
            event.widget.event_generate("<<SelectAll>>")
        if event.keycode==90: 
            event.widget.event_generate("<<Undo>>")