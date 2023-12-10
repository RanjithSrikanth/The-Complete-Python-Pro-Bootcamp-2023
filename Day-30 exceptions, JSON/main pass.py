from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_manager():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_letters = []
    password_symbols = []
    password_numbers = []

    password_letters = [random.choice(letters) for i in range(nr_letters)]
    password_symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for i in range(nr_numbers)]
    # print(password_symbols, password_numbers, password_letters)
    password_list = password_numbers + password_letters + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    pass_entry.insert(END, password)
    ##############################################Module : Pyperclip
    pyperclip.copy(password)
    # print(f"Your password is: {password}")




# ---------------------------- SAVE PASSWORD ------------------------------- #

def search():
    to_be_s = web_entry.get()
    try:
        with open("password.json", mode="r") as file:
            l_data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if to_be_s in l_data:
            email = l_data[to_be_s]["email"]
            password = l_data[to_be_s]["password"]
            # print(v["email"])
            messagebox.showinfo(title=to_be_s, message= f"Email : {email}\nPassword : {password}")
        else:
            messagebox.showinfo(title="No data Found", message=f"No details for the {to_be_s} exists")




def add():
    website = web_entry.get()
    email = name_entry.get()
    password = pass_entry.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password
        }
    }

    if len(website) < 1 or len(password) < 1:
        messagebox.showwarning(title="Not Valid", message="Please dont leave the fields empty")
    else :
        try:
            with open("password.json", mode="r") as file:
                # json.dump(new_data, file, indent=4)
                # Reading old data
                data = json.load(file)

        except:
            with open("password.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            # Saving updated data
            with open("password.json", mode="w") as file:
                json.dump(data, file, indent=4)
                # print(data)
                # file.write(f"{website} | {email} | {password}\n")

        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)

lock_i = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_i)
canvas.grid(row=0, column=1)

web_label = Label(text="Website")
web_label.grid(column=0, row=1)
uname_label = Label(text="Email / Username")
uname_label.grid(column=0, row=2)
p_label = Label(text="Password")
p_label.grid(column=0, row=3)

web_entry = Entry(width=27)
web_entry.focus()
web_entry.grid(row=1, column=1)
name_entry = Entry(width=45)
name_entry.insert(END, string="ranjith2112052@ssn.edu.in")
name_entry.grid(row=2, column=1, columnspan=2)
pass_entry = Entry(width=27)
pass_entry.grid(row=3, column=1)

button1 = Button(text="Generate Password", command=password_manager)
button1.grid(column=2, row=3)
button2 = Button(width=39, text="Add", command=add)
button2.grid(row=4, column=1,columnspan=2)
button3 = Button(text="Search", command=search, width=13)
button3.grid(column=2 , row=1)





window.mainloop()