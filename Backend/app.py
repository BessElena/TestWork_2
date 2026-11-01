from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB_NAME = 'participants.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return "Backend is working!"

# GET /api/participants — список всех участников
@app.route('/api/participants', methods=['GET'])
def get_participants():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM participants')
        rows = cursor.fetchall()
        conn.close()

        participants_list = [dict(row) for row in rows]

        return jsonify({
            "success": True,
            "data": participants_list,
            "count": len(participants_list)
        })
    except sqlite3.Error as e:
        return jsonify({
            "success": False,
            "error": "Ошибка базы данных",
            "details": str(e)
        }), 500
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Внутренняя ошибка сервера",
            "details": str(e)
        }), 500

# POST /api/participants — добавить участника
@app.route('/api/participants', methods=['POST'])
def add_participant():
    try:
        data = request.get_json() or {}

        name = data.get('name')
        email = data.get('email')
        wish = data.get('wish', '')

        # Простая валидация
        if not name or not email:
            return jsonify({
                "success": False,
                "error": "Имя и почта обязательны"
            }), 400

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO participants (name, email, wish)
            VALUES (?, ?, ?)
        ''', (name, email, wish))

        conn.commit()
        new_id = cursor.lastrowid
        conn.close()

        new_participant = {
            "id": new_id,
            "name": name,
            "email": email,
            "wish": wish
        }

        return jsonify({
            "success": True,
            "data": new_participant,
            "message": "Участник успешно добавлен"
        }), 201
    except sqlite3.Error as e:
        return jsonify({
            "success": False,
            "error": "Ошибка базы данных",
            "details": str(e)
        }), 500
    except Exception as e:
        return jsonify({
            "success": False,
            "error": "Внутренняя ошибка сервера",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, port=5000)



