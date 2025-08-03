import math
import string

def entrophy(password):
    charset = 0
    if any(c in string.ascii_lowercase for c in password):
        charset += 26
    if any(c in string.ascii_uppercase for c in password):
        charset += 26
    if any(c in string.digits for c in password):
        charset += 10
    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" for c in password):
        charset += 32

    entrophy = len(password) * math.log2(charset) if charset > 0 else 0
    return round(entrophy, 2)

def strength(password):
    ent = entrophy(password)
    if ent < 28:
        return "Very Weak", ent
    elif ent < 40:
        return "Weak", ent
    elif ent < 60:
        return "Moderate", ent
    elif ent < 80:
        return "Strong", ent
    else:
        return "Very Strong", ent
