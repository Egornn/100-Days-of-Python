import time
import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = tk.Tk()
        self.window.title(f"Quizzler")
        self.window.minsize(width=340, height=500)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.label = tk.Label(bg=THEME_COLOR, text=f"Score: {self.score}", font=("Arial", 20, 'italic'), fg="#FFFFFF")
        self.label.grid(row=0, column=1)
        self.canvas = tk.Canvas(bg="#FFFFFF", width=300, height=250)
        self.text = self.canvas.create_text(150, 125, text="There will be the question. What is this?",
                                            font=("Arial", 20, 'italic'), width=280)
        self.canvas.grid(row=1, columnspan=2, column=0, padx=(0, 10), pady=40)
        self.mark = tk.PhotoImage(file='images/true.png')
        self.cross = tk.PhotoImage(file='images/false.png')
        self.button_true = tk.Button(image=self.mark, highlightthickness=0, bg=THEME_COLOR, command=self.send_true)
        self.button_false = tk.Button(image=self.cross, highlightthickness=0, bg=THEME_COLOR, command=self.send_false)
        self.button_true.grid(row=2, column=0)
        self.button_false.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=question_text)
        else:
            self.canvas.itemconfig(self.text, text=f"Congratulation! Your final score is {self.score}/10")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def send_true(self):
        self.check_answer('true')

    def send_false(self):
        self.check_answer('False')

    def check_answer(self, answer: str):
        if self.quiz.check_answer(answer):
            self.canvas.config(bg="green")
            self.score += 1
            self.label.config(text=f"Score: {self.score}")
            print('correct')
        else:
            self.canvas.config(bg="red")
            print('False')
        self.window.after(200, self.get_next_question)
