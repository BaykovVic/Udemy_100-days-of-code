import time
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(bg="white", height=250, width=300)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=250,
            text="Some question text",
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.image_true = PhotoImage(file="images/true.png")
        self.image_false = PhotoImage(file="images/false.png")

        self.button_true = Button(image=self.image_true, highlightthickness=0, command=self.answer_true)
        self.button_true.grid(row=2, column=0)
        self.button_false = Button(image=self.image_false, highlightthickness=0, command=self.answer_false)
        self.button_false.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def answer_false(self):
       is_right = self.quiz.check_answer("False")
       self.give_feedback(is_right)
       self.score_label.config(text=f"Score: {self.quiz.score}")

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(500, self.get_next_question)


