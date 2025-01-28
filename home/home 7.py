import sqlite3
from typing import List, Tuple


def create_database():
    """Создание базы данных и таблицы products"""
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_title VARCHAR(200) NOT NULL,
        price DECIMAL(10,2) NOT NULL DEFAULT 0.0,
        quantity INTEGER NOT NULL DEFAULT 0
    )
    ''')

    conn.commit()
    conn.close()


def add_products():
    """Добавление 15 различных товаров в базу данных"""
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    products = [
        ("Жидкое мыло с запахом ванили", 75.50, 10),
        ("Мыло детское", 45.00, 15),
        ("Шампунь для волос", 120.90, 8),
        ("Зубная паста", 85.30, 12),
        ("Гель для душа", 155.75, 6),
        ("Крем для рук", 95.40, 20),
        ("Мочалка банная", 65.20, 25),
        ("Бальзам для волос", 180.60, 4),
        ("Дезодорант", 145.90, 7),
        ("Туалетная бумага", 35.80, 30),
        ("Салфетки влажные", 55.40, 18),
        ("Порошок стиральный", 245.70, 5),
        ("Кондиционер для белья", 175.30, 9),
        ("Щетка зубная", 68.90, 14),
        ("Мыло хозяйственное", 28.50, 40)
    ]

    cursor.executemany(
        "INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)",
        products
    )

    conn.commit()
    conn.close()


def update_quantity(product_id: int, new_quantity: int):
    """Изменение количества товара по id"""
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE products SET quantity = ? WHERE id = ?",
        (new_quantity, product_id)
    )

    conn.commit()
    conn.close()


def update_price(product_id: int, new_price: float):
    """Изменение цены товара по id"""
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (new_price, product_id)
    )

    conn.commit()
    conn.close()


def delete_product(product_id: int):
    """Удаление товара по id"""
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM products WHERE id = ?", (product_id,))

    conn.commit()
    conn.close()


def show_all_products():
    """Вывод всех товаров из базы данных"""
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    print("\nВсе товары в базе данных:")
    print("ID | Название | Цена | Количество")
    print("-" * 50)
    for product in products:
        print(f"{product[0]} | {product[1]} | {product[2]} | {product[3]}")

    conn.close()


def show_filtered_products(price_limit: float, quantity_limit: int):
    """Вывод товаров, которые дешевле price_limit и количество больше quantity_limit"""
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM products 
        WHERE price < ? AND quantity > ?
    """, (price_limit, quantity_limit))
    products = cursor.fetchall()

    print(f"\nТовары дешевле {price_limit} сом и количеством больше {quantity_limit} шт:")
    print("ID | Название | Цена | Количество")
    print("-" * 50)
    for product in products:
        print(f"{product[0]} | {product[1]} | {product[2]} | {product[3]}")

    conn.close()


def search_products_by_title(search_term: str):
    """Поиск товаров по названию"""
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM products 
        WHERE product_title LIKE ?
    """, (f'%{search_term}%',))
    products = cursor.fetchall()

    print(f"\nРезультаты поиска по запросу '{search_term}':")
    print("ID | Название | Цена | Количество")
    print("-" * 50)
    for product in products:
        print(f"{product[0]} | {product[1]} | {product[2]} | {product[3]}")

    conn.close()



def test_all_functions():

    create_database()
    print("База данных создана успешно")

    # add_products()
    # print("\nТовары добавлены успешно")


    show_all_products()


    update_quantity(1, 25)
    print("\nКоличество товара с ID 1 обновлено")


    update_price(2, 50.00)
    print("Цена товара с ID 2 обновлена")

    show_filtered_products(100.0, 5)


    search_products_by_title("мыло")


    delete_product(3)
    print("\nТовар с ID 3 удален")

    #
    show_all_products()


if __name__ == "__main__":
    test_all_functions()