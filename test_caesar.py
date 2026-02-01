import pytest
from cipher import caesar_encrypt, caesar_decrypt
from brute import brute_force_decrypt
from main import main
import sys

def test_caesar_encrypt():
    assert caesar_encrypt("ABC", 3) == "DEF"
    assert caesar_encrypt("xyz", 2) == "zab"
    assert caesar_encrypt("Hello, World!", 5) == "Mjqqt, Btwqi!"
    assert caesar_encrypt("Caesar Cipher", 0) == "Caesar Cipher"
    assert caesar_encrypt("Zebra", 1) == "Afcsb"

def test_caesar_decrypt():
    assert caesar_decrypt("DEF", 3) == "ABC"
    assert caesar_decrypt("zab", 2) == "xyz"
    assert caesar_decrypt("Mjqqt, Btwqi!", 5) == "Hello, World!"
    assert caesar_decrypt("Caesar Cipher", 0) == "Caesar Cipher"
    assert caesar_decrypt("Afcsb", 1) == "Zebra"

def test_brute_force_decrypt():
    encrypted_message = caesar_encrypt("Hello World", 4)
    trials = brute_force_decrypt(encrypted_message)
    assert len(trials) == 3 
    assert trials[3] == 'Ifmmp Xpsme'

    


