from cipher import caesar_decrypt
from english_words import get_english_words_set
from pyfiglet import Figlet

english_words = get_english_words_set(['web2'], lower=True)

def brute_force_decrypt(message):
    trials = {}
    for shift in range(1, 26):
        valid_word_count = 0
        print(f'Trying shift {shift}:')
        decrypted_message = caesar_decrypt(message, shift)
        words = decrypted_message.split()
        for word in words:
            if word.lower() in english_words:
                valid_word_count += 1
        if valid_word_count / len(words) >= 0.5:
            f = Figlet(font='basic')
            print(f.renderText('Found!'))
            print(f'Possible decryption with shift {shift}: {decrypted_message}')
            break
        else:
            print('No valid decryption found with this shift.\n')
        trials[shift] = decrypted_message
    return trials
