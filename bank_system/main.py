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

    def put_money(self):
        user_id = int(input("\nВведите id клиента: "))
        sum = int(input("Введите сумму которую хотите положить на счёт: "))

        cursor.execute(f"SELECT id, name, surname FROM clients WHERE id == {user_id}")
        user = cursor.fetchone()

        if user:
            cursor.execute("UPDATE clients SET balance = balance + ? WHERE id = ?", (sum, user_id))
            connect.commit()
            print(f"Баланс клиента {user} успешно пополнен")
        else:
            print("Клиента с таким id не существует!")

    def take_money(self):
        user_id = int(input("\nВведите id клиента: "))
        sum = int(input("Введите сумму которую хотите снять: "))

        cursor.execute(f"SELECT id, name, surname FROM clients WHERE id == {user_id}")
        user = cursor.fetchone()

        cursor.execute(f"SELECT balance FROM clients WHERE id == {user_id}")
        balance = cursor.fetchone()
        balance = balance[0]

        if user:
            if sum < balance:
                cursor.execute("UPDATE clients SET balance = balance - ? WHERE id = ?", (sum, user_id))
                connect.commit()
                print(f"Деньги успешно были сняты со счёта {user}")
                rest = balance - sum
                print(f"Баланс счёта составляет {rest} сом")
            else:
                print(f"На счёте {user} недостаточно средств!")
        else:
            print("Клиента с таким номером id не существует!")


client = Bank()
client.register()
client.put_money()
client.take_money()