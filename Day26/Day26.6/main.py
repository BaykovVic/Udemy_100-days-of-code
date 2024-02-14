import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

dict = {row.letter : row.code for index, row in data.iterrows()}
print(dict)

word = input("Enter a word:").upper()

output = [dict[letter] for letter in word]
print(output)