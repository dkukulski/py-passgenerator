import random

number_of_letters = int(input("How many letters in password? = "))
number_of_digits = int(input("How many digits? = "))
number_of_spec_chars = int(input("How many special characters? = "))

password = number_of_letters + number_of_spec_chars + number_of_digits

print(f"OK, the number of all characters in the password = {password}")
