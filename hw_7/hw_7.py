import sqlite3

connect = sqlite3.connect("HomeWork.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               product_title VARCHAR (200) NOT NULL,
               price REAL NOT NULL DEFAULT 0.0,
               quantity INTEGER NOT NULL DEFAULT 0)""")

def add_product():
    self_product_title = input("Введите название товара: ")
    self_price = float(input("Введите цену товара: "))
    self_quantity = int(input("Введите кол-во товара: "))

    cursor.execute(
        f"SELECT product_title FROM products WHERE product_title == '{self_product_title}'"
    )
    product_title = cursor.fetchone()

    if not product_title:
        cursor.execute(
            f"""INSERT INTO products (product_title, price, quantity)
                       VALUES ('{self_product_title}', {self_price}, {self_quantity})"""
        )
        print(f"Товар под названием {self_product_title} успешно добавлен")
    else:
        print(f"Товар по названием {self_product_title} уже существует!")

    connect.commit()

def show_product():
    cursor.execute("""SELECT * FROM products""")
    products = cursor.fetchall()
    print(products)


add_product()
show_product()