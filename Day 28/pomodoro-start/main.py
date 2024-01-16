from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✔"
ARIEL_FONT = "Arial"

reverse_count = True
count_break = True
brakes = 0
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # countdown_timer(0)
    global reverse_count
    reverse_count = False
    canvas.itemconfig(countDown_text, text=0)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reverse_count
    global reps
    reverse_count = True
    # while not reps == 4:
    countdown_timer(10)
    reps += 1

        # if reps < 4 :
        #     countdown_timer(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# def countdown_timer(count):
#
#     if count >= 0 and reverse_count:
#         canvas.itemconfig(countDown_text, text=count)
#         window.after(1000, countdown_timer, count - 1)

def countdown_timer(count):
    global reverse_count
    global count_break
    global brakes
    if count >= 0 and reverse_count:
        minutes, seconds = divmod(count, 60)
        time_format = "{:02d}:{:02d}".format(minutes, seconds)
        canvas.itemconfig(countDown_text, text=time_format)
        window.after(1000, countdown_timer, count - 1)
    else:
        countdown_timer(5)
        start_timer()
    # elif count == 1 and count_break and not brakes == 4:
    #     count_down_break()
    #
    # elif brakes == 4:
    #     reverse_count = False

    # else:
    #     reverse_count = False  # Set timer_running to False when the countdown reaches 0


# def count_down_break():
#     global brakes
#     global count_break
#     countdown_timer(10)
#     count_break = False
#     brakes += 1


# ---------------------------- UI SETUP ------------------------------- #

# Window,Title
window = Tk()
window.title("pomodoro")
canvas = Canvas(width=300, height=424, bg=YELLOW, highlightthickness=0)
window.config(padx=100, pady=50, bg=YELLOW)

# TIMER
canvas.create_text(163, 50, text="Timer", fill=GREEN, font=(ARIEL_FONT, 38, 'bold'))
canvas.grid(column=2, row=0)

# TICK
canvas.create_text(164, 390, text=TICK, fill=GREEN, font=(FONT_NAME, 18))
canvas.grid(column=2, row=9)

# Tomato Img
tomato = PhotoImage(file="tomato.png")
canvas.create_image(157, 212, image=tomato)
countDown_text = canvas.create_text(153, 230, text="00:00", fill='white', font=(FONT_NAME, 38, 'bold'))
canvas.grid(column=2, row=8)

# Buttons
start_button = Button(text="Start", font=('Ariel', 12, "bold"), width=10, command=start_timer)
start_button.grid(column=0, row=9)

reset_button = Button(text="Reset", font=('Ariel', 12, "bold"), width=10, command=reset_timer)
reset_button.grid(column=4, row=9)

window.mainloop()
