from question_bank import QuestionBank


class QuizHandler:
    def __init__(self, questions):
        self.score = 0
        self.question_count = 0
        self.is_completed = False
        self.question_bank = QuestionBank()
        self.question_bank.add_data(questions)

    def get_question_and_answer(self):
        current_question = self.question_bank.pop_question()
        if len(self.question_bank.bank) == 0:
            self.is_completed = True
        user_answer = input(f'{current_question.text}? Type "True" or "False" ')
        if user_answer == current_question.answer:
            print("Correct!")
            self.score += 1
        else:
            print('Incorrect!')
        self.question_count += 1

    def play_the_quiz(self):
        while not self.is_completed:
            self.get_question_and_answer()
            print(f"You current score is {self.score}/{self.question_count}")
        print(f"Well done! your final score is {self.score}/{self.question_count}")
