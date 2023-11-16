import turtle
import pandas
# from turtle import Turtle, Screen

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
csv_data = pandas.read_csv("50_states.csv")
all_states = csv_data.state.to_list()
# print(all_states)

# for i in csv_data["state"]:
#     if answer_s.lower() == i.lower():
#         print(i)

# game_on = True
guessed = []
while len(guessed) < 50:
    answer_s = screen.textinput(f"{len(guessed)}/50 states correct", "What's another state name ?").title()

    if answer_s == "Exit":
        not_guessed = [i for i in csv_data["state"] if i not in guessed]
        # not_guessed = []
        # for i in csv_data["state"]:
        #     if i not in guessed:
        #         not_guessed.append(i)
        data_dict = {
            "States to be learned" : not_guessed
        }
        csv =  pandas.DataFrame(data_dict)
        csv.to_csv("States_to_be_learned.csv")
        break
    if answer_s in all_states:
        guessed.append(answer_s)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        coor = csv_data[csv_data.state == answer_s]
        t.goto(int(coor.x), int(coor.y))
        t.write(answer_s)



# screen.exitonclick()

