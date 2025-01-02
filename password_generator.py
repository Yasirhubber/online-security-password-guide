import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    print("Secure Password Generator")
    length = int(input("Enter the desired password length (minimum 12): "))
    if length < 12:
        print("Password length should be at least 12 characters.")
    else:
        print("Generated Password:", generate_password(length))
