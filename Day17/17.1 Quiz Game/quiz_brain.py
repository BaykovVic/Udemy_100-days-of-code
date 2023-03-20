from question_model import Question
from data import question_data as data
from random import choice

class QuizGame:
    def __init__(self):
        self.question_bank = []
        for q_data in data:
            self.question_bank.append(Question(q_data["text"], q_data["answer"]))

    def choose_question(self):
        return choice(self.question_bank)