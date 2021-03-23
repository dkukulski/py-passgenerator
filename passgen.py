import random

number_of_letters = int(input("How many letters in password? = "))
number_of_digits = int(input("How many digits? = "))
number_of_spec_chars = int(input("How many special characters? = "))

password = number_of_letters + number_of_spec_chars + number_of_digits

print(f"OK, the number of all characters in the password = {password}")

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_"]
