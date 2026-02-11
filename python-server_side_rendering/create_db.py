#!/usr/bin/python3
""" data display with sqllite in flask"""
import sqlite3


def create_database():
    """ create a database connection to the SQLite database"""
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT NOT NULL, price REAL NOT NULL)''')

        cursor.execute('DELETE FROM products')

        data =[(1, "laptop", "electronic", 1200),
               (2, "coffe mug", "home goods",9.88),
               (3, "USB","electronic",29.99),
               (4, "Wireless Mouse", "Electronics", 25.50),
               (5, "Water Bottle", "Home Goods", 15.00),
               (6, "Monitor", "Electronics", 250.00),
               (7, "Notebook", "Stationery", 4.50)
               ]

        cursor.executemany('''INSERT INTO products(id, name, category, price) VALUES (?,?,?,?)''', data)
        conn.commit()
        conn.close()
        print("Database created successfully with 7 products")
    except sqlite3.Error as e:
        print("Database error: {}".format(e))

if __name__ == '__main__':
    create_database()
