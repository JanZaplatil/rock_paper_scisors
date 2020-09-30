import Tkinter
import tkMessageBox
import random

window = Tkinter.Tk()

# greeting text
greeting = Tkinter.Label(window, text="PLAY A GAME")
greeting.pack()

# guess entry field
guess = Tkinter.Entry(window)
guess.pack()


while True:
    myList = ["rock","paper","scisors"]

    myChoice = guess.get()
    comChoice = myList[random.randint(0,2)]


    def game():
        global result_text
        if guess.get() == "rock":
            if guess.get() == comChoice:
                result_text = " you both chose rock"
            elif comChoice == "paper":
                result_text = "you chose rock and comp paper"
            elif comChoice == "scisors":
                result_text = "you chose rock and com scisors"

        if guess.get() == "paper":
            if guess.get() == comChoice:
                result_text = " you both chose paper "
            elif comChoice == "rock":
                result_text = "you chose paper and comp paper"
            elif comChoice == "scisors":
                result_text = "you chose paper and com scisors"
        
        if guess.get() == "scisors":
            if guess.get() == comChoice:
                result_text = " you both chose scisors "
            elif comChoice == "rock":
                result_text = "you chose scisors and comp rock"
            elif comChoice == "paper":
                result_text = "you chose scisors and com paper"

        tkMessageBox.showinfo("Result", result_text)

    # submit button
    submit = Tkinter.Button(window, text="Submit", command=game)  # check_guess, not check_guess()
    submit.pack()

    window.mainloop()