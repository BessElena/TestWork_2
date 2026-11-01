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
    cursor.execute('SELECT COUNT(*) FROM participants')
    if cursor.fetchone()[0] == 0:
        test_participants = [
            ("Анна", "anna@example.com", "Хочу попасть на хакатон"),
            ("Борис", "boris@example.com", "Мечтаю выучить Flask"),
            ("Вика", "vika@example.com", "Хочется собрать крутой пет-проект")
        ]
        cursor.executemany('''
                INSERT INTO participants (name, email, wish)
                VALUES (?, ?, ?)
            ''', test_participants)
        print("Добавлены тестовые участники.")


    conn.commit()
    conn.close()
    print(f"База данных '{DB_NAME}' и таблица 'participants' готовы.")


if __name__ == '__main__':
    create_database()


