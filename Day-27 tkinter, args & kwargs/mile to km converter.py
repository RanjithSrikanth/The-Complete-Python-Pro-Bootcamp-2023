from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)
def button_click():
    input = float(entry1.get())
    answer = input * 1.609
    label1.config(text=round(answer))  # label1.config(text=f"{km}"

label1 = Label(text="0")
label1.grid(column=2, row=1)

label2 = Label(text="Miles")
label2.grid(column=3, row=0)

label3 = Label(text="is equal to")
label3.grid(column=1, row=1)

label4 = Label(text="Km")
label4.grid(column=3, row=1)

entry1 = Entry(width=10)
entry1.focus()
entry1.grid(column=2, row=0)

button1 = Button(text="Calculate", command=button_click)
button1.grid(column=2, row= 3)
window.mainloop()