import random

print("The generated password will consist of letters, numbers and special characters")
number_of_letters = int(input("How many letters? = "))
number_of_digits = int(input("How many digits? = "))
number_of_spec_chars = int(input("How many special characters? = "))

password = number_of_letters + number_of_spec_chars + number_of_digits

print(f"OK, the number of all characters in the password = {password}")

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
special_chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_"]

drawn_letters = ""
drawn_digits = ""
drawn_special_chars = ""

for letter in range(0, number_of_letters):
	drawn_letters += letters[random.randint(0, len(letters) - 1)]

for digit in range(0, number_of_digits):
	drawn_digits += digits[random.randint(0, len(digits) - 1)]

for special_char in range(0, number_of_spec_chars):
	drawn_special_chars += special_chars [random.randint(0, len(special_chars) - 1)]

signs_together = drawn_letters + drawn_digits + drawn_special_chars

# shuffling signs in password
passwd = list(signs_together)
random.shuffle(passwd)
# printing the passw
print("".join(passwd))
