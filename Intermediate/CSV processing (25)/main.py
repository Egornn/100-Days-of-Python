import turtle
from turtle import Turtle, Screen
import pandas


def coordinates_on_click(x, y):
    print(x, y)


screen = Screen()
image = "blank_states_img.gif"
screen.setup(725, 491)
screen.title("US States Game")
screen.addshape(image)
turtle.shape(image)
dataset = pandas.read_csv("50_states.csv")
correct_answers = dataset.state.to_list()
already_guessed: [str] = []
text_labels: [Turtle] = []
guessed: int = 0
answer: str = ""
while guessed < 50 and answer != "Exit":
    screen.tracer(1)
    answer = screen.textinput(title=f"Guess the State {guessed}/50",
                              prompt="What is the name of another state? Type 'Eixt' to give up")
    if answer is not None:
        answer = answer.title()
    if answer in correct_answers and not (answer in already_guessed):
        already_guessed.append(answer)
        coordinates = dataset[dataset.state == answer]
        x = int(coordinates.x.item())
        y = int(coordinates.y.item())
        text_labels.append(Turtle(visible=False))
        text_labels[-1].penup()
        text_labels[-1].goto(x, y)
        text_labels[-1].write(answer, align='center')
        guessed += 1
final_score = Turtle(visible=False)
final_score.color('black')
final_score.write(f"You have managed to guess {guessed} out of 50 states!", align='center',
                  font=("Courier", 15, "normal"))
missed_states = list(set(correct_answers) - set(already_guessed))
pandas.DataFrame(missed_states).to_csv("missed_states.csv")
turtle.onscreenclick(coordinates_on_click)
turtle.mainloop()
