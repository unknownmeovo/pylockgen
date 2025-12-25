# PyLockGen

![version](https://img.shields.io/badge/version-1.6.7-blue.svg)
![license](https://img.shields.io/badge/license-MIT-green)

**PyLockGen** is a simple and secure Python module that can:
-  Generate strong passwords
-  Calculate the entropy of a password
-  Check password strength
-  Check passwords to see if they are in the breached list 

## Installation

```
pip install pylockgen
```

## Usage
```
import pylockgen

# Generate a secure password
password = pylockgen.generate()
print(f"Generated: {password}")

# Check entropy
print("Entropy:", pylockgen.entropy(password))

# Get strength 
print("Strength:", pylockgen.strength(password))

# Check if the password is breached
print("Boolean:", pylockgen.isbreached(password)) # Returns a boolean

print(check_breach(password)) # Returns a string

```

## License
This project is licensed under the MIT License.
MIT © 2025 Hadi Raza
