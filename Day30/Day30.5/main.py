import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

dict = {row.letter : row.code for index, row in data.iterrows()}
print(dict)

#First way
is_input_done = True
while is_input_done:
    word = input("Enter a word:").upper()
    try:
        output = [dict[letter] for letter in word]
        is_input_done = False
    except KeyError as e:
        output = "Sorry, only letters are allowed"
        is_input_done = True
    else:
        is_input_done = False
    print(output)

#Another way
def generate_phonetic():
    word = input("Enter a word:").upper()
    try:
        output = [dict[letter] for letter in word]
    except KeyError as e:
        print("Sorry, only letters are allowed")
        generate_phonetic()
    else:
        print(output)

#generate_phonetic()