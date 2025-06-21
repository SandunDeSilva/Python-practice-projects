import string  # For generating the passwords
import random # For generating the random passwords

def generate_password():
    s1 = string.ascii_uppercase # To get the uppercase letters from A to Z
    s2 = string.ascii_lowercase # To get the lowercase letters from a to z
    s3 = string.digits # To get the digits from 0 to 9
    s4 = string.punctuation # To get the special characters

    password_length = int(input("Enter the password length: \n")) # To get the password length from the user

    s = [] # To create an empty list to store the characters
    s.extend(list(s1)) # To add uppercase letters to the list
    s.extend(list(s2)) # To add lowercase letters to the list
    s.extend(list(s3)) # To add digits to the list
    s.extend(list(s4)) # To add special characters to the list

    random.shuffle(s) # To shuffle the list of characters

    password = ("".join(s[0:password_length])) # To join the characters in the list to form a password
    print("Your password is: ", password) 

generate_password()