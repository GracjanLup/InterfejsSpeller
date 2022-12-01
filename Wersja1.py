import tkinter as tk
from tkinter import *
import tkinter.font as font
import time
import random

def Start():
    print(time.time())
    print(time.ctime())
    timeLabel.place(relx=0.45, rely=0.85)
    if timeleft0 == 0:
        TimerUp()
    StartButton.place_forget()
    LetterLoop()

def LetterLoop():
    global i
    if i == 23:
        Letter1.config(text="Teraz masz 5s\nna luźne mruganie", font=KiloFont)
        i = 0
        Letter1.after(5000, LetterLoop)
    else:
        Letter1.config(text=String[i], font=MegaFont)
        i+=1
        Letter1.after(1000, LetterLoop)

String = "abcdefghijklmnoprstuwyz"
timeleft0 = 0
global i
i = 0

def TimerUp():
    global timeleft0
    timeleft0 += 1
    timeLabel.config(text = str(timeleft0))
    timeLabel.after(1000, TimerUp)

root = tk.Tk()
root.title('Speller')
root.geometry('1200x800')

MegaFont = font.Font(family='Tahoma', size=400)
KiloFont = font.Font(family='Tahoma', size=80)
BigFont = font.Font(family='Tahoma', size=40)

title = Label(root, text="S p e l l e r", pady=0, font=BigFont)
title.place(x=500, y=10)

main_panel = tk.Frame(root, bg="black", highlightbackground="blue", highlightthickness=2)
main_panel.place(width=1000, height=700, relx=0.1, y=80)

timeLabel = Label(main_panel, text = str(timeleft0), font = ('Tahoma', 60), bg="white", fg="navy")

Letter1 = tk.Label(main_panel, text=String[0], font=MegaFont, fg="white", bg="black")
Letter1.place(relx=0.5, rely=0.4, anchor=CENTER)

StartButton = Button(main_panel, text="Start", bg="#222222", height=2, width=8, font=KiloFont, command=Start, fg="white")
StartButton.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
