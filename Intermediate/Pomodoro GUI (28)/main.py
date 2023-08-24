import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 3
LONG_BREAK_MIN = 7
TIMER_GLOBAL_STOP = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    text = f"{'{:02d}'.format(WORK_MIN * 60 // 60)}:{'{:02d}'.format(WORK_MIN * 60 % 60)}"
    canvas.itemconfig(timer, text=text)
    remove_marks()
    timer_txt.config(text="Timer", fg=GREEN)
    window.after_cancel(TIMER_GLOBAL_STOP)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer(how_many_iter=0):
    how_many_iter += 1
    if how_many_iter == 8:
        time_to_count = LONG_BREAK_MIN * 60
        timer_txt.config(text="Break", fg=RED)
        add_marks(how_many_iter)
        how_many_iter = 0
    elif how_many_iter % 2 == 1:
        if how_many_iter == 1:
            remove_marks()
        time_to_count = WORK_MIN * 60
        timer_txt.config(text="Work", fg=GREEN)
    else:
        time_to_count = SHORT_BREAK_MIN * 60
        timer_txt.config(text="Break", fg=PINK)
        add_marks(how_many_iter)
    countdown(time_to_count, how_many_iter)


def add_marks(iterated):
    counter.config(text="✔" * (iterated // 2))


def remove_marks():
    counter.config(text="")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count, iterative):
    global TIMER_GLOBAL_STOP
    text = f"{'{:02d}'.format(count // 60)}:{'{:02d}'.format(count % 60)}"
    canvas.itemconfig(timer, text=text)
    if count > 0:
        TIMER_GLOBAL_STOP = window.after(1000, countdown, count - 1, iterative)
    else:
        start_timer(iterative)
    # ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

timer_txt = tk.Label(text="Timer", fg=GREEN, background=YELLOW, font=(FONT_NAME, 40, 'bold'))
timer_txt.grid(row=0, column=1)

counter = tk.Label(text="", fg=GREEN, background=YELLOW, font=(FONT_NAME, 25, 'bold'))
counter.grid(row=3, column=1)

canvas = tk.Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
photo = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=photo)
timer = canvas.create_text(100, 130, text=f"{WORK_MIN}:00", fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

start = tk.Button(text="Start", width=7, highlightthickness=0, command=start_timer)
start.grid(row=2, column=0)

reset = tk.Button(text="Reset", width=7, highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

window.mainloop()
