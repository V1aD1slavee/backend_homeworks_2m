import sqlite3

connect = sqlite3.connect("Bank.db")
cursor = connect.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS clients(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR (50) NOT NULL,
               surname VARCHAR (50) NOT NULL,
               age INT NOT NULL,
               home_adress TEXT NOT NULL,
               email TEXT UNIQUE NOT NULL,
               balance INT NOT NULL DEFAULT 0,
               is_vip REAL DEFAULT False)"""
)


class Bank:
    def __init__(self):
        self.name = None
        self.surname = None
        self.age = 0
        self.home_adress = None
        self.email = None
        self.balance = 0
        self.is_vip = False

    def register(self):
        print("-------------------Введите данные пользователя-------------------")
        user_name = input("Имя: ")
        user_surname = input("Фамилия: ")
        user_age = int(input("Возраст: "))
        user_home_adress = input("Домашний адрес: ")
        user_email = input("Email: ")

        cursor.execute(f"SELECT email FROM clients WHERE email == '{user_email}'")
        user = cursor.fetchone()

        if user:
            print(f"Клиент с email адресом {user_email} уже существует!")
        else:
            cursor.execute(
                f"""INSERT INTO clients(name, surname, age, home_adress, email)
                VALUES ('{user_name}', '{user_surname}', {user_age}, '{user_home_adress}', '{user_email}')"""
            )
            connect.commit()
            print(f"Пользователь {user_name} успешно добавлен!")

client = Bank()
client.register()
