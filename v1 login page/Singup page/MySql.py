import mysql.connector as connection

  
try:
    conn=connection.connect(
        host='localhost',
        user='root',
        password='sql226611',
        database='private_notes'
        )
except:
    conn=connection.connect(
        host='localhost',
        user='root',
        password='sql226611'
        )

        

cursor=conn.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS private_notes')
cursor.execute('''CREATE TABLE IF NOT EXISTS users(
            id INT PRIMARY KEY AUTO_INCREMENT,
            username VARCHAR(15),
            password VARCHAR(15),
            email VARCHAR(40))''')
