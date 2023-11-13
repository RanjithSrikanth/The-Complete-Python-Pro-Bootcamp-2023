place_holder = "[name]"

with open("./Input/Names/invited_names.txt", mode='r') as name_file:
    names = name_file.readlines()

with open("./Input/Letters/starting_letter.txt", mode='r') as file:
    letter = file.read()
    for i in names:
        s_name = i.strip()
        new_l = letter.replace(place_holder, s_name)
        with open(f"./Output/ReadyToSend/letter_for_{s_name}", mode="w") as file:
            file.write(new_l)



