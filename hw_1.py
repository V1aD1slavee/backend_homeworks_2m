# Первое задание
class Fruits:
    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight

    def info(self):
        print(f"Название фрукта: {self.name} \nЦвет фрукта: {self.color} \nВес фрукта: {self.weight} кг")

apple = Fruits("Яблоко", "зелёное", 0.2)
banana = Fruits("Банан", "жёлтый", 0.1)
watermelow = Fruits("Арбуз", "Зелёный", 4)

apple.info()
banana.info()
watermelow.info()

# Второе задание - третье задание
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.ch_pages = "."
        self.current_page = 0

    def check_pages(self):
        if self.pages < 100:
            self.ch_pages = "тонкой"
        elif self.pages >= 100 and self.pages <= 300:
            self.ch_pages = "средней"
        else:
            self.ch_pages = "толстой"

        print(f"Книга под названием {self.title}, от автора {self.author} является {self.ch_pages}")

    def turn_page(self):
        self.current_page = int(input("Введите номер страницы на которую хотите перейти: "))
        if self.current_page <= self.pages:
            print(f"Вы находитесь на странице №{self.current_page}, книга под названием {self.title}")
        else:
            print(f"Вы не можете перейти на страницу №{self.current_page} \nтак как в {self.title} её не существует")


book1 = Book("Война и Мир", "Лев Толстой", 1274)
book2 = Book("Каштанка", "Антон Чехов", 25)
book3 = Book("Собачье сердце", "Михаил Булгаков", 160)

book1.check_pages()
book2.check_pages()
book3.check_pages()

book1.turn_page()
book1.turn_page()
book1.turn_page()
