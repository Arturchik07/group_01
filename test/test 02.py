import sqlite3


def create_database():
    conn = sqlite3.connect('store.db')
    cursor = conn.cursor()


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        code VARCHAR(2) PRIMARY KEY,
        title VARCHAR(150)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS stores (
        store_id INTEGER PRIMARY KEY,
        title VARCHAR(100)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        title VARCHAR(250),
        category_code VARCHAR(2),
        unit_price FLOAT,
        stock_quantity INTEGER,
        store_id INTEGER,
        FOREIGN KEY (category_code) REFERENCES categories(code),
        FOREIGN KEY (store_id) REFERENCES stores(store_id)
    )
    ''')


    categories_data = [
        ('FD', 'Food products'),
        ('EL', 'Electronics'),
        ('CL', 'Clothes')
    ]
    cursor.executemany('INSERT OR REPLACE INTO categories (code, title) VALUES (?, ?)',
                       categories_data)


    stores_data = [
        (1, 'Asia'),
        (2, 'Globus'),
        (3, 'Spar')
    ]
    cursor.executemany('INSERT OR REPLACE INTO stores (store_id, title) VALUES (?, ?)',
                       stores_data)


    products_data = [
        (1, 'Chocolate', 'FD', 10.5, 129, 1),
        (2, 'Jeans', 'CL', 120.0, 55, 1),
        (3, 'T-Shirt', 'CL', 8.0, 15, 1)
    ]
    cursor.executemany('''INSERT OR REPLACE INTO products 
                         (id, title, category_code, unit_price, stock_quantity, store_id) 
                         VALUES (?, ?, ?, ?, ?, ?)''', products_data)

    conn.commit()
    return conn


def display_products(cursor, store_id):
    cursor.execute('''
        SELECT p.title, c.title, p.unit_price, p.stock_quantity
        FROM products p
        JOIN categories c ON p.category_code = c.code
        WHERE p.store_id = ?
    ''', (store_id,))

    products = cursor.fetchall()
    if products:
        for product in products:
            print(f"Название продукта: {product[0]}")
            print(f"Категория: {product[1]}")
            print(f"Цена: {product[2]}")
            print(f"Количество на складе: {product[3]}")
            print()
    else:
        print("\nВ данном магазине нет продуктов.")


def main():
    conn = create_database()
    cursor = conn.cursor()

    while True:
        print(
            "Вы можете отобразить список продуктов по выбранному id магазина из "
            "перечня магазинов ниже, для выхода из программы введите цифру 0:")


        cursor.execute('SELECT store_id, title FROM stores ORDER BY store_id')
        stores = cursor.fetchall()
        for store_id, title in stores:
            print(f"{store_id}. {title}")

        try:
            choice = input("\nВведите ID магазина: ")
            if choice == '0':
                print("Программа завершена.")
                break

            store_id = int(choice)
            if store_id in [store[0] for store in stores]:
                display_products(cursor, store_id)
            else:
                print("Неверный ID магазина. Пожалуйста, выберите из списка.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")

    conn.close()


if __name__ == "__main__":
    main()