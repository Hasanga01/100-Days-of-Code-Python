from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
count = 0
is_start = True

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, width=1200, height=800)

canvas = Canvas(height=600, width=1000)

df = pd.read_csv("data/french_words.csv")

word_list = df.to_dict(orient='records')

print(word_list)


def white_box():
    canvas.delete("GreenBox")
    my_image_white = PhotoImage(file="images/card_front.png")
    canvas.create_image(500, 300, image=my_image_white, tags="whiteBox")
    canvas.config(bg=BACKGROUND_COLOR)
    canvas.grid(row=0, column=0, columnspan=3)
    # random_f_word()


def display_to_canvas():
    canvas.delete("whiteBox")
    my_image_back = PhotoImage(file="images/card_back.png")
    canvas.create_image(500, 300, image=my_image_back, tags="GreenBox")
    canvas.config(bg=BACKGROUND_COLOR)
    canvas.grid(row=0, column=0, columnspan=3)


def random_f_word():
    global count
    a = random.choice(word_list)
    french = canvas.create_text(500, 150, text="French", font=('Ariel', 42, "italic"), tags="flashcard")
    random_french_word = canvas.create_text(510, 300, text=a["French"], font=('Ariel', 60, "bold"), tags="flashcard")
    return a


def translation_word(f_word):
    print("translation started")
    canvas.delete("flashcard")
    display_to_canvas()
    english = canvas.create_text(500, 150, text="English", font=('Ariel', 42, "italic"), tags="GreenBox")
    english_translation = canvas.create_text(510, 300, text=f_word["English"], font=('Ariel', 60, "bold"),
                                             tags="GreenBox")
    print("translation text created")


def next_question():
    global count
    count += 1
    white_box()
    c_word = random_f_word()
    print(f"c word is :{c_word}")
    window.after(3000, lambda: translation_word(c_word))
    print("Waiting for 2 seconds...")

    print("translation completed")


my_image = PhotoImage(file="images/card_front.png")
canvas.create_image(500, 300, image=my_image, tags="whiteBox")
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=3)

tick_button_img = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_button_img, highlightthickness=0, command=next_question)
tick_button.grid(row=4, column=1, columnspan=2)

wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=white_box)
wrong_button.grid(row=4, column=0, columnspan=2)

window.mainloop()
