import random


class Word:
    
    def __init__(self, word_list):
        self.word = random.choice(word_list).lower()
        self.guessed_letters = set()

    def check_letter(self, letter):
        self.guessed_letters.add(letter)
        return letter in self.word
    
    def get_display_word(self):
        return " ".join(letter if letter in self.guessed_letters else '_' for letter in self.word)
    