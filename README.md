# Caesar Cipher
![Python application tests](https://github.com/Fwoopr/caesar-cipher/actions/workflows/python-app.yml/badge.svg)

A beginner-friendly Python project that implements the **Caesar Cipher** encryption technique.

This project was created for learning purposes to better understand basic cryptography concepts and simple algorithms in Python.

## What is Caesar Cipher?
The Caesar Cipher is one of the oldest encryption methods.
Each letter in the text is shifted by a fixed number of positions in the alphabet.

## Features
* Encrypt text using a given shift value
* Decrypt encrypted text with the correct shift
* Brute-force all possible shifts to decode a message without   knowing the key
* Simple and readable code, suitable for beginners

## Project Structure
```
caesar-cipher/
│
├── cipher.py        # Core encryption and decryption logic
├── brute.py         # Brute-force attack implementation
├── main.py          # Main file to run the program
├── test_caesar.py   # Basic tests for the cipher
├── pyproject.toml   # Project metadata and dependencies
├── requirements.txt
└── .gitignore
```
## Installation
**1. Clone the repository:**
```
git clone https://github.com/Fwoopr/caesar-cipher.git
```

**2. Navigate into the project folder:**
```
cd caesar-cipher
```
**3. Install dependencies:**
This project uses **pyproject.toml** for dependency management and packaging, following modern Python standards.
```
pip install .
```
**requirements.txt** is still provided for convenience.
```
pip install -r requirements.txt
```
## Usage
You can choose to either run the program **with** a shift or **without** a shift (brute force).

### With
Encrypts or decrypts the given message with the provided shift.
```
caesar 3
```
### Without
Brute forces decryption until the program finds a sentence including english words.
```
caesar
```
## Testing
The provided unit tests are written using **pytest**.
Run the test with:
```
pytest
```



