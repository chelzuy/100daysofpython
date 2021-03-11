alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(message,shift_number,func):
    show_message = ""
    if direction == "decode":
        shift_number *= -1
    for letter in message:
        count = (alphabet.index(letter)) + shift_number
        show_message += alphabet[count]
    print(f"The {func}d text is {show_message}.")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(message=text,shift_number=shift,func=direction)
