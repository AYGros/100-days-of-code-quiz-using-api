from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="question_text",
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score = Label(text="score: ", fg="white", bg=THEME_COLOR)
        self.score.grid(row=0, column=1)
        #self not needed because we dont use this again
        true = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true, command=self.choose_true)
        self.true_button.grid(row=2, column=0)
        #self not needed because we dont use this again
        false = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false, command=self.choose_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def choose_true(self):
        #same functionality as in choose false, just written differently
        self.give_feedback(self.quiz.check_answer("True"))


    def choose_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)




    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)


