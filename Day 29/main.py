import string
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(length=8):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the defined characters
    password = ''.join(random.choice(characters) for _ in range(length))
    pyperclip.copy(password)
    pw_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    valid_web = len(input_website.get())
    valid_pw = len(pw_input.get())

    if valid_web == 0 or valid_pw == 0:
        messagebox.showwarning(title="oops", message="dont leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title="Are you sure?",message=f"these are the details entered website : {input_website.get()}\n email:{email_input.get()}\n password : {pw_input.get()} \n is it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{input_website.get()} | {email_input.get()} | {pw_input.get()} \n")
            input_website.delete(0, END)
            pw_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=70)

canvas = Canvas(height=200, width=200)
photo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_img)
canvas.grid(column=2, row=2)

website_l = Label(text="Website :", font=('Ariel', 12, "bold"))
website_l.grid(column=0, row=4)

Email_l = Label(text="Email/Username :", font=('Ariel', 12, "bold"))
Email_l.grid(column=0, row=5)

password_l = Label(text="Password :", font=('Ariel', 12, "bold"))
password_l.grid(column=0, row=6)

generate_pw_btn = Button(text="Generate Password", font=('normal', 10, "bold"), width=18, command=generate_password)
generate_pw_btn.grid(column=3, row=6)
add_btn = Button(text="Add", font=('Ariel', 10, "bold"), width=50, command=save)
add_btn.grid(column=1, row=8, columnspan=3)

input_website = Entry(width=67)
input_website.grid(column=1, row=4, columnspan=3)
input_website.focus()

email_input = Entry(width=67)
email_input.grid(column=1, row=5, columnspan=3)
email_input.insert(0, "someone@example.com")

pw_input = Entry(width=41,show="•")
pw_input.grid(column=1, row=6, columnspan=2)

window.mainloop()
