from flask import Flask, request, jsonify 
import sqlite3 
import hashlib

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    
    cursor = conn.cursor()
    cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL )

''')
    
    conn.commit()
    conn.close()


def hash_password(password):
    hashlib.sha256(password.encode()).hexdigest()

init_db()

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    hashed_password = hash_password(password)

    try:
        conn = sqlite3.connect('database.db', timeout=10)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit() #salvar alteração
        conn.close() #encerrar conexão, pra evitar erros
        return jsonify( {"message": "Usuário criado com sucesso"} ), 201 
        
    except sqlite3.IntegrityError:
        return {"messagem": "Nome de usuário já está cadastrado"}, 400
    
    


if __name__ == '__main__':
    app.run()