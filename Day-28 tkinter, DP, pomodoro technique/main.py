from tkinter import *
import math

###https://stackoverflow.com/questions/11328920/is-python-strongly-typed

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#F5EA5A"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK = "✔"
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def resett():
    window.after_cancel(timer)
    canvas.itemconfig(timer_l, text="00:00")
    timer_l.config(text="Timer")
    t_label.config(text="")
    global reps
    reps = 0
# -------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_b = SHORT_BREAK_MIN * 60
    long_b = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_b)
        timer_l.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        countdown(short_b)
        timer_l.config(text="Break", fg=PINK)

    else:
        countdown(work_sec)
        timer_l.config(text="Work", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timerr, text=f"{count_min} : {count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        for i in range(math.floor(reps / 2)):
            marks += "✔"
        t_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=100, padx=50, bg=YELLOW)


timer_l = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"),bg=YELLOW)
timer_l.grid(column=1, row=0)


r_button = Button(text="Reset", command=resett)
r_button.grid(column=2, row=2)

t_label = Label(fg=GREEN, bg=YELLOW)
t_label.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
timage = PhotoImage(file="tomato.png")
canvas.create_image(100, 113, image=timage)
timerr = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


s_button = Button(text="Start", command=start_timer)
s_button.grid(column=0, row=2)

# countdown(5)



window.mainloop()
