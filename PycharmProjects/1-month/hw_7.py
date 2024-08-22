# 1. Создать базу данных hw.db в sqlite через код python, используя модуль sqlite3
#
# 2. В БД создать таблицу products
#
# 3. В таблицу добавить поле id - первичный ключ тип данных числовой и поддерживающий авто-инкрементацию.
#
# 4. Добавить поле product_title текстового типа данных максимальной длиной 200 символов, поле не должно быть пустым (NOT NULL)
#
# 5. Добавить поле price не целочисленного типа данных размером 10 цифр из которых 2 цифры после плавающей точки, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0.0
#
# 6. Добавить поле quantity целочисленного типа данных, поле не должно быть пустым (NOT NULL) значением по-умолчанию поля должно быть 0
#
# 7. Добавить функцию, которая бы добавляла в БД 15 различных товаров
#
# 8. Добавить функцию, которая меняет количество товара по id
#
# 9. Добавить функцию, которая меняет цену товара по id
#
# 10. Добавить функцию, которая удаляет товар по id
#
# 11. Добавить функцию, которая бы выбирала все товары из БД и распечатывала бы их в консоли
#
# 12. Добавить функцию, которая бы выбирала из БД товары, которые дешевле лимита по цене (100 сом) сомов и количество которых больше чем лимит остатка на складе (5 шт) и распечатывала бы их в консоли
#
# 13. Добавить функцию, которая бы искала в БД товары по названию (Например: искомое слово “мыло”, должны соответствовать поиску товары с названием - “Жидкое мыло с запахом ванили”, “Мыло детское” и тд.)
#
# 14. Протестировать каждую написанную функцию

import sqlite3


def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return connection


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_products(db_file, product):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''INSERT INTO products (product_title, price, quantity) 
                        VALUES (?, ?, ?)
            '''
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
        except sqlite3.Error as error:
            print(error)


def update_products_quantity(db_file, product):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''UPDATE products SET quantity = ?  WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
        except sqlite3.Error as error:
            print(error)


def update_products_price(db_file, product):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''UPDATE products SET price = ?  WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
        except sqlite3.Error as error:
            print(error)


def delete_products(db_file, id):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''DELETE FROM products WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
        except sqlite3.Error as error:
            print(error)


def select_all_products(db_file):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''SELECT * FROM products'''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)


def select_products_by_price_quantity(db_file, limit):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''SELECT * FROM product WHERE price <= ? AND quantity >= ?'''
            cursor = connection.cursor()
            cursor.execute(sql, limit)
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)


def select_products_by_name(connection):
    try:
        sql = '''SELECT * FROM products 
        WHERE product_title LIKE '%Kurut%'
        '''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELECT_PRODUCT_BY_NAME function')


db_name = 'hw.db'
sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL, 
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

my_connection = create_connection(db_name)
if my_connection:
    print('Connected successfully!')
    # create_table(my_connection, sql_to_create_products_table)
    # insert_products(my_connection, ('Classic Chocolate', 120.50, 7))
    # insert_products(my_connection, ('Milk Chocolate', 129.99, 3))
    # insert_products(my_connection, ('White Chocolate', 99.99, 10))
    # insert_products(my_connection, ('Black Chocolate', 150.40, 8))
    # insert_products(my_connection, ('Salted Chocolate', 145.50, 5))
    # insert_products(my_connection, ('Classic Marmalade', 89.90, 12))
    # insert_products(my_connection, ('Berry Marmalade', 100.00, 10))
    # insert_products(my_connection, ('Fruit Marmalade', 100.00, 7))
    # insert_products(my_connection, ('Classic Kurut', 30.30, 15))
    # insert_products(my_connection, ('Smoked Kurut', 35.50, 4))
    # insert_products(my_connection, ('Mint Gum', 45.80, 9))
    # insert_products(my_connection, ('Fruit Gum', 43.30, 3))
    # insert_products(my_connection, ('Cheese Chips', 150.70, 4))
    # insert_products(my_connection, ('Spicy Chips', 145.99, 7))
    # insert_products(my_connection, ('Salted Chips', 120.00, 2))
    #
    # update_products_price(my_connection, (200, 1))
    # update_products_quantity(my_connection, (15, 11))
    # delete_products(my_connection, 1)
    select_all_products(my_connection)
    # select_products_by_price_quantity(my_connection, (90, 3))
    # select_products_by_name(my_connection)
    my_connection.close()
