import sqlite3

connect = sqlite3.connect("HomeWork.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               product_title VARCHAR (200) NOT NULL,
               price DOUBLE (6,3) NOT NULL DEFAULT 0.0,
               quantity INTEGER NOT NULL DEFAULT 0)""")

def add_product():
    self_product_title = input("Введите название товара: ")
    self_price = float(input("Введите цену товара: "))
    self_quantity = int(input("Введите кол-во товара: "))
    cursor.execute(f"SELECT ")
