from question_model import Question
from data import question_data as data
from random import choice

class QuizBrain:
    def __init__(self):
        self.score = 0
        self.question_number = 0
        self.question_bank = []
        for q_data in data:
            self.question_bank.append(Question(q_data["text"], q_data["answer"]))

    def choose_question(self):
        question = self.question_bank[self.question_number]
        self.question_number += 1
        return question

    def answer_question(self, question):
        return input(f"Q.{self.question_number}: {question.text} (True/False)\n>")

    def check_answer(self, answer, question):
        if answer != question.answer:
            print("Wrooong!!!")
        else:
            self.score += 1
            print("You got it right!")

    def has_questions(self):
        if self.question_number < len(self.question_bank):
            return True
        return False

    def game_loop(self):
        while self.has_questions():
            question = self.choose_question()
            self.check_answer(self.answer_question(question), question)
            print(f"Your score is: {self.score}/{self.question_number}")
            print(f"The correct answer was {question.answer}")
        print("-------------------------------------")
        print("You've completed the quiz!")
        print(f"Your final score is {self.score}/{self.question_number}")



