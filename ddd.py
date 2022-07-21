import sqlite3
try:
    connect = sqlite3.connect('db.sqlite3')
    cursor = connect.cursor()
    #cursor.execute("""CREATE TABLE IF NOT EXISTS main_book_data(name TEXT,surname TEXT,book_title TEXT,date_lend DATE);""")
    cursor.execute("""DELETE FROM main_book_data WHERE name = "Корона";""")
    a=cursor.fetchall()
    #cursor.execute("""DROP TABLE main_book_data;""")
    cursor.close()
    connect.commit()
except:
    print('Ошибка')
finally:
    print("Я выполняюсь всегда независимо от ошибки")