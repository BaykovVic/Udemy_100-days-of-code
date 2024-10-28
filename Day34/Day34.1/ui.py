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
        pass

    def answer_false(self):
        pass

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)