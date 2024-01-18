from tkinter import *
import requests

url = "https://v2.jokeapi.dev/joke/Any"
headers = {"Accept": "application/json"}


def get_quote():
    response = requests.get("https://api.kanye.rest")
    a = response.json()["quote"]
    response.raise_for_status()
    canvas.itemconfig(quote_text, text=a)


def get_joke():
    response_t = requests.get(url)
    c = response_t.json()
    # b = response_t.json()["joke"]
    setup = c["setup"]
    delivery = c["delivery"]
    # canvas.itemconfig(quote_text, text=b)
    print(setup)
    print(delivery)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)

kanye_button.grid(row=1, column=0)

# get_quote()
get_joke()
window.mainloop()
