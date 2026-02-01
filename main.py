import sys
from pyfiglet import Figlet
from cipher import caesar_encrypt, caesar_decrypt
from brute import brute_force_decrypt


def main():
    f = Figlet(font='slant')
    print(f.renderText('Caesar Cipher'))
    if len(sys.argv) == 2:
        answer = input("Would you like to (e)ncrypt or (d)ecrypt a message? e/d ").strip().lower()
        if not answer in ['e', 'd']:
            sys.exit("Invalid option. Please enter 'e' to encrypt or 'd' to decrypt.")
        if answer == 'e':
            try:
                message = input("Enter the message to encrypt: ").strip()
                encrypted_message = caesar_encrypt(message, shift=sys.argv[1])
                print("Encrypted message:", encrypted_message)
            except ValueError:
                sys.exit('Shift must be an integer.')
        elif answer == 'd':
            try:
                message = input("Enter the message to decrypt: ").strip()
                decrypted_message = caesar_decrypt(message, shift=sys.argv[1])
                print("Decrypted message:", decrypted_message)
            except ValueError:
                sys.exit('Shift must be an integer.')
    else:
        print("No shift value provided. Starting brute-force decryption.")
        message = input("Enter the message to brute force: ").strip()
        trials = brute_force_decrypt(message)
        answer = input("Would you like to see all attempted decryptions? (y/n) ").strip().lower()
        while True:
            if answer in ['y', 'n']:
                break
            answer = input("Please enter 'y' or 'n': ").strip().lower()
        if answer == 'y':
            for shift in range(1, len(trials) + 1):
                print(f'Shift {shift}: {trials[shift]}')


        
        

if __name__ == "__main__":
    main()