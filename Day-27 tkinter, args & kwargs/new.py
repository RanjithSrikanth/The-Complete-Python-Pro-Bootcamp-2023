from tkinter import *


def button_clicked():
    print("i got clicked")
    user = einput.get()
    label1.config(text=user)


windoww = Tk()
windoww.title("Ranjith")
windoww.minsize(500, 500)

# label
label1 = Label(text="Sample text")
label1.grid(column=0, row=0)
# button
btton1 = Button(text="Click here !!!", command=button_clicked)
btton1.grid(column=1, row=1)
# btton1.pack()

button2 = Button(text="click here")
button2.grid(column=2, row=0)

# entry
einput = Entry(width=10)
print(einput.get())
einput.grid(column=3, row=2)
# einput.pack()


windoww.mainloop()
