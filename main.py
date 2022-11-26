import tkinter as tk
from tkinter import *
import tkinter.font as font
import time
import random
from PIL import Image, ImageTk, ImageFilter

def ClickLetter():
    print("Hey!")

def Pointer():
    key_fields[44].config(image=test1)

def PointerUp():
    print("Up")

def PointerDown():
    print("Down")

def PointerLeft():
    print("Left")

def PointerRight():
    print("Right")

number_of_rows=6
number_of_columns=15
number_of_fields = number_of_rows*number_of_columns

root = tk.Tk()
root.title('Speller')
root.geometry('1200x800')

BigFont = font.Font(family='Tahoma', size=40)
TextFont = font.Font(family='Tahoma', size=20)

main_panel = tk.Frame(root, bg="grey")
main_panel.place(width=1000, height=700, relx=0.1, rely=0.1)

keyboard = tk.Frame(root, bg="black")
keyboard.place(width=840, height=340, relx=0.17, rely=0.2)

letter = Image.open("Grafiki/a.png")
letter = letter.resize((50,50))
test = ImageTk.PhotoImage(letter)

letterRed = Image.open("Grafiki/a_p.png")
letterRed = letterRed.resize((50,50))
test1 = ImageTk.PhotoImage(letterRed)

title = Label(root, text="S p e l l e r", pady=10, font=BigFont)
title.place(x=500, y=10)

LeftPause = Button(main_panel, text="Luźne \nmruganie", bg="white", height=20, width=5)
LeftPause.place(x=20, y=80)
RightPause = Button(main_panel, text="Luźne \nmruganie", bg="white", height=20, width=5)
RightPause.place(x=930, y=80)
BottomPause = Button(main_panel, text="Luźne \nmruganie", bg="white", height=3, width=120)
BottomPause.place(x=90, y=430)

UpArrow = Button(main_panel, text="^", bg="white", height=5, width=5, command=PointerUp)
UpArrow.place(x=700, y=500)
DownArrow = Button(main_panel, text="v", bg="white", height=5, width=5, command=PointerDown)
DownArrow.place(x=700, y=550)
RightArrow = Button(main_panel, text=">", bg="white", height=5, width=5, command=PointerRight)
RightArrow.place(x=750, y=550)
LeftArrow = Button(main_panel, text="<", bg="white", height=5, width=5, command=PointerLeft)
LeftArrow.place(x=650, y=550)

key_fields = [tk.Button(keyboard, image=test, bg="#141414", command=ClickLetter) for i in range(number_of_fields)]

for i in range(number_of_columns):
    for j in range(number_of_rows):
        key_fields[i * number_of_rows + j].grid(row = j, column = i)

Pointer()
root.mainloop()
