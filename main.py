import tkinter as tk
from tkinter import *
import tkinter.font as font
import time
import random
from PIL import Image, ImageTk, ImageFilter
from functools import partial

# Tabela indeksów rozkładu graficznego przycisków:
# * - * - * - *
# 5 - 0 - 2 - 6
# 5 - 1 - 3 - 7
# - - 8 8 8 - -

# Funkcja po kliknięciu(mrugnięciu) w grupę
def ClickGroup(i):
    print(i)
    # Zapominenie umieszczenia odpowiedniego przycisku grupy
    group_fields[i].grid_forget()
    # Funkcja dla przycisku z indeksem 0
    if i == 0:
        # Funkcja w funkcji dla klinkięcia literki z utworzonej tablicy:
        #  - na razie usuwa tylko wszystkie przyciski po kliknięciu,
        def ClickLetter():
            for i in range(len(key_fields)):
                key_fields[i].grid_forget()
            print("Łakamaka")

        # definiowanie zmiennych dla pierwszej tabeli (i=0)
        number_of_rows=2
        number_of_columns=4
        number_of_fields = number_of_rows*number_of_columns

        # stworzenie okna pierwszej tabeli (i=0)
        Frame0 = tk.Frame(keyboard, bg="black")
        Frame0.place(width=445, height=170)

        # definiowanie pierwszego łańcucha liter
        String0 = "abcdefg-"

        # definiowanie tabeli przycisków
        key_fields = [tk.Button(Frame0, text=String0[i], font=TextFont, bg="white", command=ClickLetter, height=2, width=6) for i in range(number_of_fields)]

        # ułożenie tych przycisków
        for i in range(number_of_columns):
            for j in range(number_of_rows):
                key_fields[i * number_of_rows + j].grid(row = j, column = i)
        # usunięcię przycisku z "-"
        key_fields[7].grid_forget()
    elif i == 1:
        # praktycznie wszystko to samo co dla i=0 tylko dla i=1 (lewa dolna grupa)
        def ClickLetter():
            for i in range(len(key_fields)):
                key_fields[i].grid_forget()
            print("Łakamaka")

        number_of_rows=2
        number_of_columns=3
        number_of_fields = number_of_rows*number_of_columns

        Frame1 = tk.Frame(keyboard, bg="black")
        Frame1.place(width=445, height=170, y=170)

        String1 = "opqrst"

        key_fields = [tk.Button(Frame1, text=String1[i], font=TextFont, bg="white", command=ClickLetter, height=2, width=6) for i in range(number_of_fields)]

        for i in range(number_of_columns):
            for j in range(number_of_rows):
                key_fields[i * number_of_rows + j].grid(row = j, column = i)
    elif i == 2:
        # praktycznie wszystko to samo co dla i=0 tylko dla i=2 (prawa górna grupa)
        def ClickLetter():
            for i in range(len(key_fields)):
                key_fields[i].grid_forget()
            print("Łakamaka")

        number_of_rows=2
        number_of_columns=4
        number_of_fields = number_of_rows*number_of_columns

        Frame2 = tk.Frame(keyboard, bg="black")
        Frame2.place(width=445, height=170, x=445)

        String2 = "hijklmn-"

        key_fields = [tk.Button(Frame2, text=String2[i], font=TextFont, bg="white", command=ClickLetter, height=2, width=6) for i in range(number_of_fields)]

        for i in range(number_of_columns):
            for j in range(number_of_rows):
                key_fields[i * number_of_rows + j].grid(row = j, column = i)
        key_fields[7].grid_forget()
    else:
        # praktycznie wszystko to samo co dla i=0 tylko dla i=3 (prawa dolna grupa)
        def ClickLetter():
            for i in range(len(key_fields)):
                key_fields[i].grid_forget()
            print("Łakamaka")

        number_of_rows=2
        number_of_columns=3
        number_of_fields = number_of_rows*number_of_columns

        Frame3 = tk.Frame(keyboard, bg="black")
        Frame3.place(width=445, height=170, x=445, y=170)

        String3 = "uvwxyz"

        key_fields = [tk.Button(Frame3, text=String3[i], font=TextFont, bg="white", command=ClickLetter, height=2, width=6) for i in range(number_of_fields)]

        for i in range(number_of_columns):
            for j in range(number_of_rows):
                key_fields[i * number_of_rows + j].grid(row = j, column = i)

# Początkowe ustawienie pointera
def Pointer():
    group_fields[0].config(bg="red")

# Funkcja dla przesuwania pointera w górę
def PointerUp():
    global pointer_location
    # case1 pointer jest na grupach dolnych (i=1 lub 3)
    if pointer_location == 1 or pointer_location == 3:
        group_fields[pointer_location].config(bg="white")
        pointer_location-=1
        group_fields[pointer_location].config(bg="red")
    # case2 pointer jest na luzie dolnym (i=8)
    elif pointer_location == 8:
        BottomPause.config(bg="white")
        pointer_location=1
        group_fields[pointer_location].config(bg="red")
    # case3 pointer jest na luzie prawym (i=7)
    elif pointer_location == 7:
        RightPause.config(bg="white")
        pointer_location=6
        BackSpace.config(bg="red")
    # w pozostałych przypadkach funkcja nie robi nic
    else:
        pass

# Funkcja dla przesuwania pointera w dół
def PointerDown():
    global pointer_location
    # case1 pointer jest na grupach górnych (i=0 lub 2)
    if pointer_location == 0 or pointer_location == 2:
        group_fields[pointer_location].config(bg="white")
        pointer_location+=1
        group_fields[pointer_location].config(bg="red")
    # case2 pointer jest na grupach dolnych (i=1 lub 3)
    elif pointer_location == 1 or pointer_location == 3:
        group_fields[pointer_location].config(bg="white")
        pointer_location=8
        BottomPause.config(bg="red")
    # case3 pointer jest na backspace (i=6)
    elif pointer_location == 6:
        BackSpace.config(bg="white")
        pointer_location=7
        RightPause.config(bg="red")
    # pozostałe nie robi nic
    else:
        pass

# Funkcja dla przesuwania pointera w lewo
def PointerLeft():
    global pointer_location
    # case1 pointer jest na grupach prawych (i=2 lub 3)
    if pointer_location == 2 or pointer_location == 3:
        group_fields[pointer_location].config(bg="white")
        pointer_location-=2
        group_fields[pointer_location].config(bg="red")
    # case2 pointer jest na backspace lub luzie prawym (i=6 lub 7)
    elif pointer_location == 6 or pointer_location == 7:
        BackSpace.config(bg="white")
        RightPause.config(bg="white")
        pointer_location-=4
        group_fields[pointer_location].config(bg="red")
    # case3 pointer jest na grupach lewych (i=0 lub 1)
    elif pointer_location == 0 or pointer_location == 1:
        group_fields[pointer_location].config(bg="white")
        pointer_location=5
        LeftPause.config(bg="red")
    else:
        pass

def PointerRight():
    global pointer_location
    # case1 pointer jest na grupach lewych (i=0 lub 1)
    if pointer_location == 0 or pointer_location == 1:
        group_fields[pointer_location].config(bg="white")
        pointer_location+=2
        group_fields[pointer_location].config(bg="red")
    # case2 pointer jest na grupie prawej górnej (i=2)
    elif pointer_location == 2:
        group_fields[pointer_location].config(bg="white")
        pointer_location=6
        BackSpace.config(bg="red")
    # case3 pointer jest na grupie prawej dolnej (i=3)
    elif pointer_location == 3:
        group_fields[pointer_location].config(bg="white")
        pointer_location=7
        RightPause.config(bg="red")
    # case4 pointer jest luzie lewym (i=5)
    elif pointer_location == 5:
        LeftPause.config(bg="white")
        pointer_location=0
        group_fields[pointer_location].config(bg="red")
    else:
        pass

# ustawienie pozucji pointera jako zmiennej globalnej
global pointer_location
pointer_location=0

# utworzenie okna tkintera
root = tk.Tk()
root.title('Speller')
root.geometry('1200x800')

# Szablonów czcionek
BigFont = font.Font(family='Tahoma', size=40)
TextFont = font.Font(family='Tahoma', size=20)

# Głównego okna akcji
main_panel = tk.Frame(root, bg="grey", highlightbackground="blue", highlightthickness=2)
main_panel.place(width=1000, height=700, relx=0.1, y=80)

# Okna grup i klawiatury
keyboard = tk.Frame(root, bg="black")
keyboard.place(width=840, height=340, relx=0.17, rely=0.2)

# Tytuł
title = Label(root, text="S p e l l e r", pady=0, font=BigFont)
title.place(x=500, y=10)

# Luźne mruganie
LeftPause = Button(main_panel, text="Luźne \nmruganie", bg="white", height=20, width=8)
LeftPause.place(x=10, y=80)
RightPause = Button(main_panel, text="Luźne \nmruganie", bg="white", height=10, width=8)
RightPause.place(x=925, y=250)
BottomPause = Button(main_panel, text="Luźne \nmruganie", bg="white", height=3, width=120)
BottomPause.place(x=80, y=420)

# BackSpace
BackSpace = Button(main_panel, text="<x", bg="white", height=4, width=3, font=TextFont)
BackSpace.place(x=930, y=80)

# Strzałki
UpArrow = Button(main_panel, text="^", bg="white", height=6, width=10, command=PointerUp)
UpArrow.place(x=700, y=480)
DownArrow = Button(main_panel, text="v", bg="white", height=6, width=10, command=PointerDown)
DownArrow.place(x=700, y=580)
RightArrow = Button(main_panel, text=">", bg="white", height=6, width=10, command=PointerRight)
RightArrow.place(x=780, y=580)
LeftArrow = Button(main_panel, text="<", bg="white", height=6, width=10, command=PointerLeft)
LeftArrow.place(x=620, y=580)

# Textbox
WrittenText = Text(main_panel, height = 1, width = 30, font=TextFont)
WrittenText.place(x=290, y=5)

# Grupy liter:
# partial pozwala wysłać zmienną w aktywacji przycisku.
group_fields = [tk.Button(keyboard, text="a, b, c, d,\ne, f, g", font=BigFont, bg="white", command=partial(ClickGroup, 0), height=2, width=15), tk.Button(keyboard, text="h, i, j, k,\nl, m, n", font=BigFont, bg="white", command=partial(ClickGroup, 1), height=2, width=15),
tk.Button(keyboard, text="o, p, q,\nr, s, t", font=BigFont, bg="white", command=partial(ClickGroup, 2), height=2, width=14),
tk.Button(keyboard, text="u, v, w,\nx, y, z", font=BigFont, bg="white", command=partial(ClickGroup, 3), height=2, width=14)]
# Ułożenie przycisków grup liter
for i in range(2):
    for j in range(2):
        group_fields[i * 2 + j].grid(row = j, column = i, sticky=W+E)

Pointer()
root.mainloop()
