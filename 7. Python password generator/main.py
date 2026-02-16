import random
import string

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(alphabet)

    return password

length = input("How long would you like your password to be? ")

try:
    length = int(length)
    generated_password = generate_password(length)

    print("Your password is: " + generated_password)
except ValueError:
    print("You did not give an integer value!")