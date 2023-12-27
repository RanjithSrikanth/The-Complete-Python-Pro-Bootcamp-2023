from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.label1 = Label(text=f"Score", bg=THEME_COLOR, fg="white")
        self.label1.grid(column=1, row=0)
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.canvas = Canvas(width=300, height=250)
        self.question = self.canvas.create_text(150, 125, text="Something", fill=THEME_COLOR
                                                , font=("Arial", 20, "italic"), width=290)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        image1 = PhotoImage(file="images/true.png")
        self.button1 = Button(image=image1, highlightthickness=0, command=self.right)
        self.button1.grid(column=0, row=2, pady=10, padx=10)

        image2 = PhotoImage(file="images/false.png")
        self.button2 = Button(image=image2, highlightthickness=0, command=self.wrong)
        self.button2.grid(column=1, row=2)

        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.label1.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question, text="You've reached end of the quiz !!")
            self.button1.config(state="disabled")
            self.button2.config(state="disabled")
    def right(self):

        self.givefeedback(self.quiz.check_answer("True"))
            # self.canvas.config(bg="green")
            #
            # self.next_question()
            # self.canvas.config(bg="white")

    def wrong(self):

        self.givefeedback(self.quiz.check_answer("False"))
        # if self.quiz.check_answer("False"):
        #     print("False")

    def givefeedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.next_question)