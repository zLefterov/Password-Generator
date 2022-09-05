#python password generator

#store all characters in a list
#ask the user to add password length
#shuffle characters via random.shuffle method
#initialize an emptry list to store the password
#Loop that iterates length times
#-pick random characters from random.choice
#-append the random characters to the password
#shuffle the password list to make it more random
#convert password list to string
#print the generated password

import string
import random

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')
def generate_random_password():
    length = int(input("How long the generated password should be: "))
    random.shuffle(characters) 
    password = [] 
    for i in range(length): 
        if i < 5: 
            print("Are you sure that short password will be good for you?")
    else i > 8:
        print("That's a good start for a strong password! Good job!")            
        password.append(random.choice(characters))
    random.shuffle(password)     
    print(''.join(password))
generate_random_password()