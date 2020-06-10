from tkinter import *
import math

def comicFont():
    return "Comic Sans MS"

def showResultWord(event):
    textBoxHeightNew = float(textBoxHeight.get()) / 100
    result = float(textBoxWeight.get())/math.pow(float(textBoxHeightNew),2)
    result = float("{:.2f}".format(result))
    if result > 30:
        resultCalculate.configure(text=(result, "Very obesity"), fg="red")
    elif float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2) >= 25:
        resultCalculate.configure(text=(result, "obesity"), fg="#EA4492")
    elif float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2) >= 23:
        resultCalculate.configure(text=(result, "Overweight"), fg="#FE7A15")
    elif float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2) >= 18.6:
        resultCalculate.configure(text=(result, "Normal"), fg="green")
    elif float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2) < 18.6:
        resultCalculate.configure(text=(result, "Underweight"), fg="purple")


mainWindow = Tk()
programName = Label(mainWindow,text = "IBM Calculator",font = ("Impact",20),bg = "yellow")
programName.grid(row = 0)
labelHeight = Label(mainWindow,text = "Height (cm) :",font = (comicFont(),20),bg = "#A8E6CE")
labelHeight.grid(row = 1, column = 0)
labelWeight = Label(mainWindow,text = "Weight (Kg) :",font = (comicFont(),20),bg = "#A8E6CE")
labelWeight.grid(row = 2, column = 0)
textBoxHeight = Entry(mainWindow,font = (comicFont(),20))
textBoxHeight.grid(row =1, column = 1)
textBoxWeight = Entry(mainWindow,font = (comicFont(),20))
textBoxWeight.grid(row =2, column = 1)
buttonCalculate = Button(mainWindow,text = "Calculate!!",font =("Impact",15),fg = "#E8175D",bg ="#DCEDC2" )
buttonCalculate.grid(row = 3, column = 0)
buttonCalculate.bind('<Button-1>',showResultWord)
resultCalculate = Label(mainWindow,text = "Result",font = ("Impact",15),fg = "black",bg = "#F9CDAD",width = 30)
resultCalculate.grid(row = 3, column = 1)
mainWindow.mainloop()
