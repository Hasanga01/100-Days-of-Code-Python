from tkinter import *

window = Tk()

window.title("Miles to KM", )
window.minsize(300, 200)
window.config(padx=50, pady=50)


def convert():
    km = round(int(input_box.get()) * 1.6, 2)
    label_ans = Label(text=km, font=('Ariel', 12, "bold"))
    # inp_label.config(padx=100,pady= 200)
    label_ans.grid(column=1, row=5)
    label_ans.config(pady=30)


label = Label(text="Miles", font=('Ariel', 12, "bold"))
# inp_label.config(padx=100,pady= 200)
label.grid(column=0, row=0)
label.config(padx=10)

input_box = Entry(width=12)
input_box.grid(column=1, row=0)

label_km = Label(text="KM", font=('Ariel', 12, "bold"))
# inp_label.config(padx=100,pady= 200)
label_km.grid(column=0, row=5)
label_km.config(pady=30)

button = Button()
button.config(text="Convert", font=('Ariel', 12, "bold"), width=10, command=convert)
button.grid(column=1, row=7)

window.mainloop()
