#!/usr/bin/env python3
import Tkinter
from Tkinter import *
import tkMessageBox
import random

window = Tkinter.Tk()

# greeting text
greeting = Tkinter.Label(window, text="PLAY A GAME")
greeting.pack()

# guess entry field
guess = Tkinter.Entry(window)
guess.pack()

my_list = ["rock","paper","scisors"]

def game():
    my_choice = guess.get()
    com_choice = my_list[random.randint(0,2)]
    
    if my_choice == "rock":
        if my_choice == com_choice:
            result_text = " you both chose rock"
        elif com_choice == "paper":
            result_text = "you chose rock and comp paper"
        elif com_choice == "scisors":
            result_text = "you chose rock and comp scisors"

    if my_choice == "paper":
        if my_choice == com_choice:
            result_text = " you both chose paper "
        elif com_choice == "rock":
            result_text = "you chose paper and comp rock"
        elif com_choice == "scisors":
            result_text = "you chose paper and comp scisors"
    
    if my_choice == "scisors":
        if my_choice == com_choice:
            result_text = " you both chose scisors "
        elif com_choice == "rock":
            result_text = "you chose scisors and comp rock"
        elif com_choice == "paper":
            result_text = "you chose scisors and comp paper"

    tkMessageBox.showinfo("Result", result_text)

submit = Tkinter.Button(window, text="Submit", command=game)  # check_guess, not check_guess()
submit.pack()

while True:
    window.mainloop()
