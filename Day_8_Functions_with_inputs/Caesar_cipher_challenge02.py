from typing import Counter


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(message, shift_number):
    new_message = ""

    for letter in message:
        count = (alphabet.index(letter)) + shift_number
        new_message += alphabet[count]
    print(f"The encoded text is {new_message}.")
    
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decrypt(new_message,shift_number):
    
  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet 
  # by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
    message = ""
    for letter in new_message:
        count_back = (alphabet.index(letter)) - shift_number
        message += alphabet[count_back]
    print(f"The decode text is {message}")
      
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. 
# Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt 
# *AND* decrypt a message.

if direction == "encode":
    encrypt(message=text,shift_number=shift)
elif direction == "decode":
    decrypt(new_message=text,shift_number=shift)