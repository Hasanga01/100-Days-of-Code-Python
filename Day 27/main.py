from tkinter import *

window = Tk()
window.title("MY first GUI")

window.minsize(600, 600)
window.config(padx=200,pady=200)

my_label = Label(text="I am a label", font=('Ariel', 22, "bold"))
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="New Text")


def got_clicked():
    # my_label["text"] = "New Text"
    my_label.config(text=f"{input_e.get()}")


button = Button(text='click Me', command=got_clicked)
button.grid(column=1, row=1)

button2 = Button(text='New Button', command=got_clicked)
button2.grid(column=0, row=2)

input_e = Entry(width=12)
input_e.grid(column=3, row=3)
c = input_e.get()

window.mainloop()
