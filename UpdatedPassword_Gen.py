
import string

import random


#Asks the user how long they would like their password to be
def main():

    global numChar

    char = input("How many characters would you like your password to be?")

    try:
        numChar = int(char)
    except ValueError:
        print("Please enter a number!")
        main()

    question()


#Asks the user if they would like uppercase or lowercase letters
def question():

    global answer

    answer = input("Would you like lowercase letters, or uppercase letters?(l/u)")

    upper_lower()




#Prints out the users random password if they choose the uppercase letters
def main_upper(numChar):
    print("Your password is")
    print("----------------")

    for x in range(numChar):
        password = ''.join(random.choice(string.ascii_uppercase + string.digits))
        new_pass = (str(password))
        print(new_pass, end = " ")

    end()


#Prints out the users random password if they choose the lowercase letters
def main_lower(numChar):

    print("Your password is")
    print("----------------")

    for x in range(numChar):
        password = ''.join(random.choice(string.ascii_lowercase + string.digits))
        new_pass = (str(password))
        print(new_pass, end = " ")

    end()

#Checks if the user wanted uppercase or lowercase letters, and runs the proper function
def upper_lower():

    global answer

    if answer == "l":
        main_lower(numChar)
    elif answer == "u":
        main_upper(numChar)
    elif answer != "l" or "u":
        print("please input 'u' or 'l'")
        question()
    end()

#Asks the user if they would like to generate another password
def end():
    print("\n")
    another_one = input("Would you like to generate another password?(y/n)")
    if another_one == "y":
        main()
        question()
    elif another_one == "n":
        quit()
    else:
        print("please choose 'y' or 'n'")
        end()


main()
question()
main_upper()
main_lower()
upper_lower()
end()
