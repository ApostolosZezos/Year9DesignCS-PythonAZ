import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label
import subprocess
import threading
import webbrowser
import os
import tkinter.font as tkFont


root = tk.Tk()
root.title("Command Term Dictionary v1.0")
root.configure(background = '#E6EBEE')


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def clearIbDefText():
	IbDefText.delete(1.0,tk.END)

def clearSimpleDefText():
	SimpleDef.delete(1.0,tk.END)


#********************************************** Center root Window ****************************************************

w = 520
h = 410

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

#********************************************** Accesibility Functions ****************************************************

def AccessibilityContrast():
	root.config(bg= "#002B81")
	selectCommandTerm.config(bg = "#FF5F00")
	AccessibilityButton.config(highlightbackground = "#FFFA00")
	FontChange.config(highlightbackground = "#FFFA00")
	LinkButton.config(highlightbackground = "#FFFA00")
	RubricButton.config(highlightbackground = "#FFFA00")
	ibDefLabel.config(bg = "#C10000", font = "Times 23")
	IbDefText.configure(bg = "#FFB800", highlightbackground = "#000000", font = "fixedsys 18")
	simpleDefLabel.config(bg = "#C10000", font = "Times 23")
	simpleDef.configure(bg = "#FFB800", highlightbackground = "#000000", font = "fixedsys 18")
	exampleBox.configure(bg = "#FFB800", highlightbackground = "#000000")
	submitButton.config(highlightbackground = "#FFFA00")
	ClearButton.config(highlightbackground = "#FFFA00")
	Website.config(highlightbackground = "#FFFA00")

def NormalContrast():
	root.config(bg= "#E6EBEE")
	selectCommandTerm.config(bg = "#0856DB")
	AccessibilityButton.config(highlightbackground = "#07329D")
	FontChange.config(highlightbackground = "#07329D")
	LinkButton.config(highlightbackground = "#07329D")
	RubricButton.config(highlightbackground = "#07329D")
	ibDefLabel.config(bg = "#69B4E1", font = "Times 23")
	IbDefText.configure(bg = "#CBE7F8", highlightbackground = "#009299", font = "fixedsys 18")
	simpleDefLabel.config(bg = "#69B4E1", font = "Times 23")
	simpleDef.configure(bg = "#CBE7F8", highlightbackground = "#009299", font = "fixedsys 18")
	exampleBox.configure(bg = "#CBE7F8", highlightbackground = "#009299")
	submitButton.config(highlightbackground = "#0856DB")
	ClearButton.config(highlightbackground = "#0856DB")
	Website.config(highlightbackground = "#07329D")

#Coulour Storage

#white = "CBE7F8"
#dark = "043E61"
#blue = "2F93CF"
#light blue = "69B4E1"

#********************************************** Drop down menu: IB definitions ****************************************************

ibDefs = ["Give a detailed account or\npicture of a situation, event,\npattern or process", "Make an appraisal by\nweighing up the strengths\nand limitations", "Give valid reasons or\nevidence to support an\nanswer or a conclusion"]

def test1(event):
	#global ibDefs
	#global IbDefText
	IbDefText.delete(1.0, tk.END)

	if event == 'Describe':
		#print(str(ibDefs[0]))
		IbDefText.insert(tk.INSERT, str(ibDefs[0]))
	elif event == 'Evaluate':
		#print(str(ibDefs[1]))
		IbDefText.insert('end', str(ibDefs[1]))
	elif event == 'Justify':
		#print(str(ibDefs[2]))
		IbDefText.insert('end', str(ibDefs[2]))
#********************************************** Drop down menu: Simple definitions ****************************************************

simpleDefs = ["Present characteristics of a\nparticullar topic with lots\nof detail", "What can or cannot be done? Make a judgement", "Why was this chosen as the\nresponse/answer?"]

def test2(event):
	#simpleDef.insert(0, tk.END)
	simpleDef.delete(1.0, tk.END)
	if event == 'Describe':
		#print(str(simpleDefs[0]))
		simpleDef.insert(tk.END, simpleDefs[0])
	elif event == 'Evaluate':
		#print(str(simpleDefs[1]))
		simpleDef.insert("end", simpleDefs[1])
	elif event == 'Justify':
		#print(str(simpleDefs[2]))
		simpleDef.insert(tk.END, simpleDefs[2])

#********************************************** Extra Functions ****************************************************

#************************************************ Example Entry Window ****************************************************

def submit():
	global entry
	global entry2
	submitWin = tk.Tk()
	submitWin.title("Submit Examples")


	title = tk.Label(submitWin, text="Use this format(name, date, class, teacher)", height = 2, width = 50)
	title.grid(row = 0, column = 0)

	entry = tk.Entry(submitWin)
	entry.grid(row = 1, column = 0)

	title2 = tk.Label(submitWin, text="Enter Example Question, (colen) :, Answer", height = 2, width = 50)
	title2.grid(row = 2, column = 0)

	entry2 = tk.Entry(submitWin)
	entry2.grid(row = 3, column = 0)

	submit = tk.Button(submitWin, text = "Submit", height = 2, width = 50, command = combine_funcs(save, submitWin.destroy))
	submit.grid(row = 4, column = 0)

#************************************************ Save to .txt file and Rewrite it  ****************************************************

def save():
	person = entry.get()
	question = entry2.get()
	f = open("save.txt", "a")
	f.write( "\n" + person + "\n" + question)
	f.close()

def clear():
	f = open("save.txt", "w")
	f.write( "[CLEARED: New Content]" )
	f.close()

	# print(event)
	# print(commandTerm.get())
	# ibDefListbox.delete(0, tk.END)
	# ibDefListbox.insert(tk.END, commandTerm.get() +  ": \n Test Definition")
	# simpleDefListbox.delete(0, tk.END)
	# simpleDefListbox.insert(tk.END, commandTerm.get() + ": \n Test Definition")

#************************************************ FIRST ROW ****************************************************

#************************************************ Dropdown Menu ****************************************************

commandTerm = tk.StringVar(root)
commandTerm.set("Command Terms") 
selectCommandTerm = tk.OptionMenu(root, commandTerm, "Describe", "Evaluate", "Justify", command = combine_funcs(test1, test2))
selectCommandTerm.config(bg = "#0856DB",  height = 2, width = 14)
selectCommandTerm.grid(row = 0, column = 2, columnspan = 2, sticky = "N")

#************************************************ Accesibility Button ****************************************************

AccessibilityButton = tk.Button(root, text="High Contrast", height = 3, command = AccessibilityContrast)
AccessibilityButton.config(highlightbackground = "#07329D")
AccessibilityButton.grid(row = 0, column = 0)

#************************************************ Normal Contrast ****************************************************

FontChange = tk.Button(root, text="Normal Colours", height = 3, command = NormalContrast)
FontChange.config(highlightbackground = "#07329D")
FontChange.grid(row = 0, column = 1)

#************************************************ All Rubrics Link ****************************************************

new = 1
url1 = "https://www.easthartford.org/uploaded/ciba/Academics/All_MYP_Year_5_Assessment_Criteria_and_Rubrics.pdf"

def openweb():
    webbrowser.open(url1,new=new)

LinkButton = tk.Button(root, text="All Rubrics", height = 3, command = openweb)
LinkButton.config(highlightbackground = "#07329D")
LinkButton.grid(row = 0, column = 4)

#************************************************ Rubric Breakdown Button ****************************************************

new = 1
url2 = "https://lh3.googleusercontent.com/TEouDE5ABkl4g1ap8G7PQdyJbCNfKxDwdDCjZQ4dkD5NmwQIQe3Opxt0ldqVUUp6720_Ukss9NBLxSi9Sk_Q5oGbz41V8Qsmsi36qR06YZC0sGSyk08n=w572"

def openweb():
    webbrowser.open(url2,new=new)

RubricButton = tk.Button(root, text="Rubric's\nBreakdown", height = 3, command = openweb)
RubricButton.config(highlightbackground = "#07329D")
RubricButton.grid(row = 0, column = 5)

#************************************************ SECOND ROW ****************************************************

#************************************************ IB definition label ****************************************************

ibDefLabel = tk.Label(root, text="IB Definition", width = 19, height =1)
ibDefLabel.config(bg = "#69B4E1", font = "Times 23")
ibDefLabel.grid(row = 1, column = 0, columnspan = 3, pady = 6)


IbDefText = tk.Text(root, height = 4, width = 20)
IbDefText.configure(state = "normal", bg = "#CBE7F8", highlightbackground = "#009299", font = "fixedsys 18")
IbDefText.grid(row = 2, column = 0, columnspan = 3, padx = 3)

#************************************************ Simple Definition Label ****************************************************

simpleDefLabel = tk.Label(root, text="Simple Definition", width = 19, height =1)
simpleDefLabel.config(bg = "#69B4E1", font = "Times 23")
simpleDefLabel.grid(row = 1, column = 3, columnspan = 5)


simpleDef = tk.Text(root, width = 20, height = 4)
simpleDef.configure(state = "normal", bg = "#CBE7F8", highlightbackground = "#009299", font = "fixedsys 18")
simpleDef.grid(row = 2, column = 3, columnspan = 3, padx = 5)

#************************************************ Scrollbar and Example display ****************************************************

#commentsListbox = tk.Listbox(root, width = 44, height = 10)
#commentsListbox.insert(i1data)
#commentsListbox.grid(row = 3, column = 0, rowspan = 2, columnspan = 5, padx = 10, pady = 10)

scrollbar = tk.Scrollbar(root)
scrollbar.grid(row = 3, column = 5, rowspan = 2, sticky = "E")

exampleBox = tk.Text(root, width = 49, height = 8)
exampleBox.configure(state = "normal", bg = "#CBE7F8", highlightbackground = "#009299", font = "fixedsys 15")
exampleBox.grid(row = 3, column = 0, columnspan = 6, padx = 5, pady = 8, sticky = "W")

exampleBox.insert('end', open("save.txt",'r').read())


exampleBox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = exampleBox.yview)

#************************************************ Submit Example Button ****************************************************

submitButton = tk.Button(root, text="Submit", height = 2, width = 8, command = submit)
submitButton.config(highlightbackground = "#0856DB")
submitButton.grid(row = 5, column = 4)

#************************************************ Clear Example File Button ****************************************************

ClearButton = tk.Button(root, text = "Clear",  height = 2, width = 8, command = clear)
ClearButton.config(highlightbackground = "#0856DB")
ClearButton.grid(row = 5, column = 5)

#************************************************ Developer's Website Link ****************************************************
new = 1
url3 = "https://sites.google.com/ucc.on.ca/year9designcoding-azezos/unit-1/developing-ideas?authuser=0"

def openweb():
    webbrowser.open(url3, new = new)

Website = tk.Button(root, text = "Developer's Website", height = 2, width = 39, command = openweb)
Website.config(highlightbackground = "#07329D")
Website.grid(row = 5, column = 0, columnspan = 4)




root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.mainloop()
