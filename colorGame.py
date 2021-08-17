# Programmer - python_scripts (Inlinesam)


import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox


timeleft = 60
score = 0



def CreateWidgets():

    instLabel = Label(root, text = "ENTER COLOR OF THE TEXT",
                      font = ('Helvetica',30),background = 'WHITE')
    instLabel.grid(row = 0, column = 0, columnspan = 3, padx=5, pady=15)

    startButton = Button(root, text = "START GAME", width = 20,
                font = ('Helvetica',15), command = StartGame, background='WHITE')
    startButton.grid(row = 1, column = 0,padx = 5,pady = 15, columnspan = 3 )

    root.timeLabel = Label(root, text="TIME LEFT : ", font = ('Helvetica',30),
                           background='WHITE')
    root.timeLabel.grid(row=2, column=0, padx=5, pady=15)

    root.scoreLabel = Label(root, text="SCORE : "+str(score),
                            font = ('Helvetica',30),background = 'WHITE')
    root.scoreLabel.grid(row=2, column=1, padx=5, pady=15)

    root.gameLabel = Label(root, font = ('Comic Sans MS',60),background = 'WHITE')
    root.gameLabel.grid(row = 3, column = 0, padx=5, pady=15, columnspan = 2)

    root.answerEntry = Entry(root,width = 50, font =30,background = 'SILVER')
    root.answerEntry.grid(row=4, column=0, padx=5, pady=15, columnspan = 2)
    root.answerEntry.focus()


def StartGame():
   
    global timeleft, score

   
    if timeleft > 0:
       
        timeleft -= 1
        
        root.timeLabel.config(text="TIME LEFT : " + str(timeleft))

      
        randomColor = ['RED', 'GREEN', 'BLUE', 'VIOLET', 'PINK', 'BROWN', 'BLACK','CYAN','YELLOW','ORANGE']
     
        random.shuffle(randomColor)

       
        root.gameLabel.config(text=str(randomColor[0]), fg=randomColor[1])



        if root.answerEntry.get().lower() == randomColor[1].lower():
            
            score += 1
            
            root.scoreLabel.config(text = "SCORE : "+str(score))
            
            root.answerEntry.delete(0, END)

        
        root.timeLabel.after(1000, StartGame)

   
    else:
        messagebox.showinfo("TIME UP !","YOUR SCORE IS : "+str(score))




root = tk.Tk()


root.title("PythonColor Game")
root.configure(background = 'WHITE')
root.resizable(False, False)


CreateWidgets()


root.mainloop()

