from question_model import Question
from data import question_data
from random import randint


class QuestionBank:
    def __init__(self):
        self.bank = []

    def __str__(self):
        string_rep = []
        for question in self.bank:
            string_rep.append(question.text)
        return str(string_rep)

    def add_data(self, questions_as_list_of_dictionary):
        for quest in questions_as_list_of_dictionary['results']:
            self.bank.append(Question(quest["question"], quest['correct_answer']))

    def pop_question(self):
        if len(self.bank) == 0:
            return Question("", "True")
        return self.bank.pop(randint(0, len(self.bank)-1))



