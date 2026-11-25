from english_words import get_english_words_set
import random

def generate_random_word():
    words = get_english_words_set(['web2'], lower=True)

    five_letter_word = []

    for word in words:  
        if len(word) == 5:
            five_letter_word.append(word)
        
    random_word = random.choice(five_letter_word)
    # print(random_word)

    return random_word