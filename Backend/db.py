import sqlite3

DB_NAME = 'participants.db'

def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Создаём таблицу participants
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS participants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            wish TEXT
        )
    ''')



    conn.commit()
    conn.close()
    print(f"База данных '{DB_NAME}' и таблица 'participants' готовы.")


if __name__ == '__main__':
    create_database()


