# Encryption and Decryption Functions

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesar_encrypt(message, shift):
    encrypted_message = []
    for char in message:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_message.append(alphabet[(index + int(shift)) % len(alphabet)])
        elif char in alphabet.lower():
            index = alphabet.index(char.upper())
            encrypted_message.append(alphabet[(index + int(shift)) % len(alphabet)].lower())
        else:
            encrypted_message.append(char)
    encrypted_message = ''.join(encrypted_message)

    return encrypted_message

def caesar_decrypt(message, shift):
        decrypted_message = []
        for char in message:
            if char in alphabet:
                index = alphabet.index(char)
                decrypted_message.append(alphabet[(index - int(shift)) % len(alphabet)])
            elif char in alphabet.lower():
                index = alphabet.index(char.upper())
                decrypted_message.append(alphabet[(index - int(shift)) % len(alphabet)].lower())
            else:
                decrypted_message.append(char)
        decrypted_message = ''.join(decrypted_message)

        return decrypted_message