import random
import string

def genPassword(length=8, use_uppercase = True, use_digits = True, use_symbols = True):

    if length < 4:
        raise ValueError("Password length must be at least 4")

    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"

    return ''.join(random.choice(characters) for _ in range(length))

