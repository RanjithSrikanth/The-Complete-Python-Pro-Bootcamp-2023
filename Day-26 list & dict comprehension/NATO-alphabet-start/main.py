import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(data)

df = pandas.DataFrame(data)
dictt = {row.letter : row.code for (index, row) in df.iterrows()}

ui = input("Enter a word : ").upper()
result = [dictt[i] for i in ui]
print(result)
