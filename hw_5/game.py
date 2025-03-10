from word import Word

class Game:
    def __init__(self):
        word_list = ["ябоко","банан","Пайтон","море","акула"]
        self.word = Word(word_list)
        self.attemps = 7

    def play(self):
        print("Привет. Добро пожаловать в нашу игру!")
        print("Суть игры угадать слово по буквам!")
        print(f"Так же у вас ограниченное кол-во попыток: {self.attemps}")

        while self.attemps > 0:
            print(f"\nCлово: {self.word.get_display_word()}")
            letter = input("Введите букву: ").lower()

            if self.word.check_letter(letter):
                print("Верно")
                print("[--------------------------]")
            else:
                self.attemps -= 1
                print(f"Неверно! Осталось попыток: {self.attemps}")
                print("[--------------------------]")

            if "_" not in self.word.get_display_word():
                print(f"Поздравляем вы угадали слово!\nСлово: {self.word.word}")
                return

        print(f"Вы проиграли! Загаданное слово: {self.word.word}")

if __name__ == "__main__":
    game = Game()
    game.play()
