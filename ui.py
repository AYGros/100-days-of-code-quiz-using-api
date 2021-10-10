from tkinter import *


THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="question_text", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = Label(text="score: ", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)
        #self not needed because we dont use this again
        true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true)
        self.true_button.grid(row=2, column=0)
        #self not needed because we dont use this again
        false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false)
        self.false_button.grid(row=2, column=1)





        self.window.mainloop()