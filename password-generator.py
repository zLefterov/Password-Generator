#python password generator
import string
import random

#store all characters in a list
characters = list(string.ascii_letters + string.digits + '!@#$%^&*()')

#ask the user to add password length
def generate_random_password():
    length = int(input("How long the generated password should be: "))

    random.shuffle(characters) #shuffle characters via random.shuffle method

    password = [] #initialize an emptry list to store the password

    for i in range(length): #Loop that iterates length times.
        if i < 5: 
            print("Are you sure that short password will be good for you?")
    else i > 8:
        print("That's a good start for a strong password! Good job!")
            

    #-pick random characters from random.choice
    #-append the random characters to the password
        password.append(random.choice(characters))

    random.shuffle(password) #shuffle the password list to make it more random

    #convert password list to string
    #print the generated password
    print(''.join(password))
generate_random_password()