import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

df = pandas.DataFrame(data)
dictt = {row.letter : row.code for (index, row) in df.iterrows()}

def generate():
    ui = input("Enter a word : ").upper()
    try:
        result = [dictt[i] for i in ui]
    except KeyError :
        print("Sorry, only alphabets willl be accessses")
        generate()
    else:
        print(result)

generate()