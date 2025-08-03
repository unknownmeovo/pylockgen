import math
import string

def entropy(password):
    charset = 0
    if any(c in string.ascii_lowercase for c in password):
        charset += 26
    if any(c in string.ascii_uppercase for c in password):
        charset += 26
    if any(c in string.digits for c in password):
        charset += 10
    if any(c in "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" for c in password):
        charset += 32

    entropy = len(password) * math.log2(charset) if charset > 0 else 0
    return round(entropy, 2)

def strength(password):
    ent = entropy(password)
    if ent < 28:
        return "Very Weak"
    elif ent < 40:
        return "Weak"
    elif ent < 60:
        return "Moderate"
    elif ent < 80:
        return "Strong"
    else:
        return "Very Strong"

