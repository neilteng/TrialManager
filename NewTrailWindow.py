import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from tinydb import TinyDB
import NewDate, UsedDate, LoadLastTrailNumber, UpdateTrailNumber, CtrlKeys, LoadSetup
import json
from pprint import pprint
import os

# def on_configure(event):
# 	# update scrollregion after starting 'mainloop'
# 	# when all widgets are in canvas
# 	global canvas
# 	canvas.configure(scrollregion=canvas.bbox('all'))


def NewTrailWindow(isNewDate, wd):
	global editor
	editor = tk.Tk()
	editor.title('New a Trail')
	editor.geometry("1300x1050")

	# Create a database or connect to one
	db = TinyDB('./resources/db.json')

	date = None
	if isNewDate:
		date = NewDate.newDate()
	else:
		date = UsedDate.usedDate()

	global trail_number
	trail_number = int(LoadLastTrailNumber.lastTrailNumber())
	print("trail_number: "+ str(trail_number))

	# Date Notice
	DateInfo = tk.Text(editor, height=1)
	DateInfo.insert(1.0, "Current trails are under date folder: " + date)
	# tk.Label(editor, text = "Current trails are under date folder: " + date , font=("Arial", 15))
	DateInfo.configure(bg=editor.cget('bg'), relief="flat", font=("Times New Roman", 15, "bold"))
	DateInfo.configure(state="disabled")
	DateInfo.grid(row=0, column=0, columnspan = 2, padx=20,pady=20)


	# Create Text Boxes
	TrialSetup = ScrolledText(editor, width=50, height=15, undo=True, autoseparators=True, maxundo=-1)
	TrialSetup.bind("<Control-KeyPress>", CtrlKeys.ctrlKeys)
	TrialSetup.grid(row=1, column=0, padx=(150,0), pady=20, columnspan = 2)
	TrialSetup.configure(font=("Times New Roman", 16, "bold"))
	
	# default example
	TrialSetup.insert('1.0', "{\n\"Ca\":30,\n\"Na\":100,\n\"fps\": 4\n}")

	# import from file
	def importFromFile():
		TrialSetup.delete("1.0","end")
		TrialSetup.insert( '1.0',
			LoadSetup.loadSetup(
				filedialog.askopenfilename(parent = editor, initialdir = wd, title="select a setup file")
			)
		)

	# button 
	newButton = tk.Button(editor, text="Create a new Trail", command = lambda: newTrail(TrialSetup, ShowTrails, db, date, wd))
	newButton.grid(row=2, column=0, padx=(600,0), pady=20 )
	newButton.configure(font=("Times New Roman", 12, "bold"))

	importButton = tk.Button(editor, text="import a setup", command = importFromFile )
	importButton.grid(row=2, column=0,padx=(0,0), pady=20)
	importButton.configure(font=("Times New Roman", 12, "bold"))

	ShowTrails = ScrolledText(editor, width=60, height=10)

	ShowTrails.configure(bg=editor.cget('bg'), relief="flat", font=("Times New Roman", 10, "bold"))
	ShowTrails.grid(row=3, column=0, padx=50, pady=10, columnspan = 2)
	ShowTrails.configure(font=("Times New Roman", 12, "bold"))

def newTrail(TrialSetup, ShowTrails, db, date, wd):
	inputValue=TrialSetup.get("1.0","end-1c")
	
	# pprint(json.loads(inputValue))

	global trail_number
	global editor
	setup = json.loads(inputValue)

	# show file name
	setupStr = "_".join([key+'_'+str(setup[key]) for key in setup.keys()])
	ShowTrails.configure(state="normal")
	file_dir = str(date)+ "/trail" + '_' + str(trail_number) + '_' + setupStr
	ShowTrails.insert('1.0', file_dir+'\n')
	ShowTrails.configure(state="disabled")

	# insert into db
	db.insert({'date': date, "trail_number": trail_number, "setup": setup, "file_dir": file_dir})

	os.makedirs(os.path.join(wd+'/./'+file_dir))
	# print(os.path.join(wd+'/./'+file_dir))
	# # increase trial number each time pushing the button
	trail_number+=1
	UpdateTrailNumber.updateTrailNumber(trail_number)

	