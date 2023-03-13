alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(message, shift_amount):
    cipher_text = ""
    for letter in message:
        position = alphabet.index(letter)
        if position + shift_amount > len(alphabet):
            new_position = position + shift_amount - len(alphabet)
        else:
            new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    return cipher_text

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(message, shift_amount):
    cipher_text = ""
    for letter in message:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    return cipher_text
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
direction = ""
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'exit':
        exit(0)
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == 'encode':
        print(encrypt(text, shift))
    elif direction == 'decode':
        print(decrypt(text, shift))