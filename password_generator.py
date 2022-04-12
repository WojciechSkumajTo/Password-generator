#!/usr/local/bin/python3

import sys
import random
import string

password = []

character_left = -1


def give_conditions_password():
    lowercase_letters = int(input("Please enter how many small characters:"))
    check_lenght(lowercase_letters)
    uppercase_letters = int(input("Please enter how many big characters:"))
    check_lenght(uppercase_letters)
    special_characters = int(
        input("Please enter how many special characters:"))
    check_lenght(special_characters)
    digits = int(input("Please eneter how many numbers:"))
    check_lenght(digits)
    return lowercase_letters, uppercase_letters, special_characters, digits


def check_lenght(lenght_letters):
    global character_left
    if lenght_letters < 0 or lenght_letters > character_left:
        print("The terms of the password do not match its length")
        print("Characters range (0, ", character_left, ">")
        sys.exit(0)
    else:
        character_left -= lenght_letters
        print("Characters range (0,", character_left, ">")


def check_lenght_character_left(lowercase_letters):
    global character_left
    if character_left:
        lowercase_letters += character_left
        print(lowercase_letters)
        return lowercase_letters
    else:
        print(lowercase_letters)
        print("All free characters have been used")
        return lowercase_letters


def show_detail(lowercase_letters, uppercase_letters, special_characters, digits):
    print("Lowercase: ", lowercase_letters)
    print("Uppercase:", uppercase_letters)
    print("Special characters:", special_characters)
    print("Digits: ", digits)


def check_lenght_conditions(length):
    if length:
        return True
    else:
        return False


def password_generation(
    lowercase_letters, uppercase_letters, special_characters, digits
):
    global password
    for i in range(password_lenght):
        if check_lenght_conditions(lowercase_letters):
            password.append(random.choice(string.ascii_lowercase))
            lowercase_letters -= 1
        if check_lenght_conditions(uppercase_letters):
            password.append(random.choice(string.ascii_uppercase))
            uppercase_letters -= 1
        if check_lenght_conditions(special_characters):
            password.append(random.choice(string.punctuation))
            special_characters -= 1
        if check_lenght_conditions(digits):
            password.append(random.choice(string.digits))
            digits -= 1


def password_mix():
    global password
    random.shuffle(password)


def main():
    (
        lowercase_letters,
        uppercase_letters,
        special_characters,
        digits,
    ) = give_conditions_password()
    lowercase_letters = check_lenght_character_left(lowercase_letters)
    show_detail(lowercase_letters, uppercase_letters,
                special_characters, digits)
    password_generation(lowercase_letters, uppercase_letters,
                        special_characters, digits)
    password_mix()

    print("--------------------------------")
    passw = "".join(password)
    print(f"Your passsword is: {passw}")


if __name__ == '__main__':
    password_lenght = int(input("Please enter the password length: "))
    if password_lenght < 5:
        print("Password is too short! Please eneter new length")
        print("Password must have at least 5 characters")
        sys.exit(0)
    else:
        character_left = password_lenght
    main()
