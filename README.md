# PyLockGen

[![PyPI version](https://badge.fury.io/py/pylockgen.svg)](https://pypi.org/project/pylockgen/)

PyLockGen is a secure password generator and strength checker module written in Python.

## Features

- Generate strong random passwords
- Check strength using entropy
- Simple and lightweight

## Installation

```
pip install pylockgen
```

## Usage 

```
import pylockgen

pwd = pylockgen.generate(length=16)
strength, entropy = pylockgen.strength(pwd)

print("Password:", pwd)
print("Strength:", strength)
print("Entropy:", entropy)

```

## License

MIT © 2025 Hadi Raza
