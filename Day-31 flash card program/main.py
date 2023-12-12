from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
dict_data = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original = pandas.read_csv("data/french_words.csv")
    dict_data = original.to_dict(orient="records")
else:
    dict_data = data.to_dict(orient="records")
current_card = {}
# print(dict_data)
# data_dict = {
#     data["french"] : data["english"]
# }

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict_data)
    canvas.itemconfig(c_title, text="French", fill="black")
    canvas.itemconfig(c_word, text=current_card["French"], fill="black")
    # flip_card()
    canvas.itemconfig(imagee, image=front)
    flip_timer = window.after(3000, func=flip_card)
    # canvas.itemconfig()

def flip_card():
    canvas.itemconfig(imagee, image=back)
    canvas.itemconfig(c_title ,text = "English", fill="white")
    canvas.itemconfig(c_word, text=current_card["English"], fill="white")

def known():
    dict_data.remove(current_card)
    # print(len(dict_data))
    data = pandas.DataFrame(dict_data)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
flip_timer = window.after(3000, func=flip_card)



canvas = Canvas(width=800, height=526)
front = PhotoImage(file="images/card_front.png")
imagee = canvas.create_image(400, 263, image=front)
back = PhotoImage(file="images/card_back.png")
# canvas.create_image(400, 263, image=back)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
c_title = canvas.create_text(400, 150, text="Title", font=('Arial', 40, 'italic'))
c_word = canvas.create_text(400, 250, text="word", font=('Arial', 40, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

image1 = PhotoImage(file="images/right.png")
button1 = Button(image=image1, highlightthickness=0, command=known)
button1.grid(row=1, column=1)

image2 = PhotoImage(file="images/wrong.png")
button2 = Button(image=image2, highlightthickness=0, command=next_card)
button2.grid(row=1, column=0)

next_card()




window.mainloop()

