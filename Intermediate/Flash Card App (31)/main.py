import tkinter as tk
import pandas as p
from pandas import DataFrame


def get_words_bank(path: str):
    data = p.read_csv(path)
    dictionary_list = data.to_dict(orient='records')
    keys = list(dictionary_list[0].keys())
    print(keys)
    language_to_learn = keys[0]
    language_to_translate = keys[1]
    # words_to_learn


get_words_bank('data/french_words.csv')

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.title('Flash Cards')
window.minsize(width=880, height=726)
window.config(background=BACKGROUND_COLOR, pady=50, padx=50)

card_back = tk.PhotoImage(file='images/card_back.png')
card_front = tk.PhotoImage(file='images/card_front.png')
right = tk.PhotoImage(file='images/right.png')
wrong = tk.PhotoImage(file='images/wrong.png')

canvas = tk.Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 268, image=card_front)
canvas_label = canvas.create_text(400, 180, text="French", font=("Ariel", 40, 'italic'))
canvas_word = canvas.create_text(400, 293, text="Trouve", font=("Ariel", 60, 'bold'))
canvas.grid(columnspan=2, row=0, column=0)

yes_button = tk.Button(image=right, highlightthickness=0, background=BACKGROUND_COLOR)
no_button = tk.Button(image=wrong, highlightthickness=0, background=BACKGROUND_COLOR)
yes_button.grid(row=1, column=0)
no_button.grid(row=1, column=1)

window.mainloop()
