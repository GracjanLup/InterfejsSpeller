import tkinter as tk
from tkinter import *
import tkinter.font as font
import time
import random
from PIL import Image, ImageTk, ImageFilter

def ClickLetter():
    print("Hey!")

def Pointer():
    group_fields[0].config(bg="red")

def PointerUp():
    global pointer_location
    if pointer_location == 1 or pointer_location == 3:
        group_fields[pointer_location].config(bg="white")
        pointer_location-=1
        group_fields[pointer_location].config(bg="red")
    elif pointer_location == 8:
        BottomPause.config(bg="white")
        pointer_location=1
        group_fields[pointer_location].config(bg="red")
    elif pointer_location == 7:
        RightPause.config(bg="white")
        pointer_location=6
        BackSpace.config(bg="red")
    else:
        pass

def PointerDown():
    global pointer_location
    if pointer_location == 0 or pointer_location == 2:
        group_fields[pointer_location].config(bg="white")
        pointer_location+=1
        group_fields[pointer_location].config(bg="red")
    elif pointer_location == 1 or pointer_location == 3:
        group_fields[pointer_location].config(bg="white")
        pointer_location=8
        BottomPause.config(bg="red")
    elif pointer_location == 6:
        BackSpace.config(bg="white")
        pointer_location=7
        RightPause.config(bg="red")
    else:
        pass

def PointerLeft():
    global pointer_location
    if pointer_location == 2 or pointer_location == 3:
        group_fields[pointer_location].config(bg="white")
        pointer_location-=2
        group_fields[pointer_location].config(bg="red")
    elif pointer_location == 6 or pointer_location == 7:
        BackSpace.config(bg="white")
        RightPause.config(bg="white")
        pointer_location-=4
        group_fields[pointer_location].config(bg="red")
    elif pointer_location == 0 or pointer_location == 1:
        group_fields[pointer_location].config(bg="white")
        pointer_location=5
        LeftPause.config(bg="red")
    else:
        pass

def PointerRight():
    global pointer_location
    if pointer_location == 0 or pointer_location == 1:
        group_fields[pointer_location].config(bg="white")
        pointer_location+=2
        group_fields[pointer_location].config(bg="red")
    elif pointer_location == 2:
        group_fields[pointer_location].config(bg="white")
        pointer_location=6
        BackSpace.config(bg="red")
    elif pointer_location == 3:
        group_fields[pointer_location].config(bg="white")
        pointer_location=6
        RightPause.config(bg="red")
    elif pointer_location == 5:
        LeftPause.config(bg="white")
        pointer_location=0
        group_fields[pointer_location].config(bg="red")
    else:
        pass

number_of_rows=6
number_of_columns=15
number_of_fields = number_of_rows*number_of_columns
global pointer_location
pointer_location=0

root = tk.Tk()
root.title('Speller')
root.geometry('1200x800')

BigFont = font.Font(family='Tahoma', size=40)
TextFont = font.Font(family='Tahoma', size=20)

main_panel = tk.Frame(root, bg="grey", highlightbackground="blue", highlightthickness=2)
main_panel.place(width=1000, height=700, relx=0.1, rely=0.1)

keyboard = tk.Frame(root, bg="black")
keyboard.place(width=840, height=340, relx=0.17, rely=0.2)

# letter = Image.open("Grafiki/a.png")
# letter = letter.resize((50,50))
# test = ImageTk.PhotoImage(letter)
#
# letterRed = Image.open("Grafiki/a_p.png")
# letterRed = letterRed.resize((50,50))
# test1 = ImageTk.PhotoImage(letterRed)

title = Label(root, text="S p e l l e r", pady=10, font=BigFont)
title.place(x=500, y=10)

LeftPause = Button(main_panel, text="Luźne \nmruganie", bg="white", height=20, width=5)
LeftPause.place(x=40, y=80)
RightPause = Button(main_panel, text="Luźne \nmruganie", bg="white", height=10, width=5)
RightPause.place(x=930, y=250)
BottomPause = Button(main_panel, text="Luźne \nmruganie", bg="white", height=3, width=120)
BottomPause.place(x=80, y=420)

BackSpace = Button(main_panel, text="<x", bg="white", height=4, width=3, font=TextFont)
BackSpace.place(x=930, y=80)

UpArrow = Button(main_panel, text="^", bg="white", height=6, width=10, command=PointerUp)
UpArrow.place(x=700, y=480)
DownArrow = Button(main_panel, text="v", bg="white", height=6, width=10, command=PointerDown)
DownArrow.place(x=700, y=580)
RightArrow = Button(main_panel, text=">", bg="white", height=6, width=10, command=PointerRight)
RightArrow.place(x=780, y=580)
LeftArrow = Button(main_panel, text="<", bg="white", height=6, width=10, command=PointerLeft)
LeftArrow.place(x=620, y=580)

# group_fields = [tk.Button(keyboard, text="a", font=BigFont, bg="white", command=ClickLetter, height=2, width=14) for i in range(4)]
group_fields = [tk.Button(keyboard, text="a, b, c, d,\ne, f, g", font=BigFont, bg="white", command=ClickLetter, height=2, width=15), tk.Button(keyboard, text="h, i, j, k,\nl, m, n", font=BigFont, bg="white", command=ClickLetter, height=2, width=15),
tk.Button(keyboard, text="o, p, q,\nr, s, t", font=BigFont, bg="white", command=ClickLetter, height=2, width=14),
tk.Button(keyboard, text="u, v, w,\nx, y, z", font=BigFont, bg="white", command=ClickLetter, height=2, width=14)]

for i in range(2):
    for j in range(2):
        group_fields[i * 2 + j].grid(row = j, column = i, sticky=W+E)

# for i in range(number_of_columns):
#     for j in range(number_of_rows):
#         group_fields[i * number_of_rows + j].grid(row = j, column = i)

Pointer()
root.mainloop()
