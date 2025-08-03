# PyLockGen

![version](https://img.shields.io/badge/version-1.3.1-blue.svg)
![license](https://img.shields.io/badge/license-MIT-green)

**PyLockGen** is a simple and secure Python module that can:
-  Generate strong passwords
-  Calculate entropy of a password
-  Check password strength

## Installation

```
pip install pylockgen
```

## Usage
```
import pylockgen

# Generate a secure password
password = pylockgen.generate()
print("Generated:", password)

# Check entropy
print("Entropy:", pylockgen.entropy(password))

# Get strength 
print("Strength:", pylockgen.strength(password))

```

## License
This project is licensed under the MIT License.
