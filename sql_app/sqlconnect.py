import sqlite3
conn=sqlite3.connect("sql_app.db")

conn.execute('''
Create table if not exists User(
    user_id INT PRIMARY KEY,
    email VARCHAR(30) UNIQUE,
    hashed_password VARCHAR(50)
 
)
''')

conn.execute('''
Create table if not exists Product(
    product_id VARCHAR(105) PRIMARY KEY,
    title VARCHAR(30),
    description VARCHAR(50),
    price INT           
)
''')

conn.close()