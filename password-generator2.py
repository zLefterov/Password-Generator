# Password generator with additional control and requirements

# Characters to generate password from
# Password lenght set by the user
# Password characters
# init the password
# Picking random alphabets, digits, special characters

import string
import random

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list('!@#$%^&*()')
characters = list(string.ascii_letters + string.digits + '!@#$%^&*()') #improvisation

def generate_random_password():
    length = int(input("How long the password should be? : "))
    alphabets_count = int(input("How many alphabets you'd like to be included? : "))
    digital_count = int(input("How many digits you'd like to have in the password? : "))
    special_characters_count = int(input("How many special characters you'd like to be included? : "))

    characters_count = alphabets_count + digital_count + special_characters_count

    if characters_count > length:
        print("The total number of characters is greater than the password length - end of program")
        return
    
    password = []
    for i in range(alphabets_count):
        password.append(random.choice(alphabets))
    
    for i in range(digital_count):
        password.append(random.choice(digits))
    
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    if characters_count < length:
          random.shuffle(characters)
          for i in range(length - characters_count):
            password.append(random.choice(characters))
    random.shuffle(password)

    print("".join(password))

#call the function
generate_random_password()  

