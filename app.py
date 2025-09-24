from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_PATH = 'database.db'

# Crea tabella se non esiste
with sqlite3.connect(DB_PATH) as conn:
    conn.execute('''
        CREATE TABLE IF NOT EXISTS phrases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phrase TEXT NOT NULL
        )
    ''')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phrase = request.form.get('phrase')
        if phrase:
            with sqlite3.connect(DB_PATH) as conn:
                conn.execute('INSERT INTO phrases (phrase) VALUES (?)', (phrase,))
        return redirect(url_for('index'))

    # Recupera tutte le frasi
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute('SELECT id, phrase FROM phrases')
        phrases = cursor.fetchall()
    return render_template('index.html', phrases=phrases)

@app.route('/delete/<int:phrase_id>', methods=['POST'])
def delete_phrase(phrase_id):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('DELETE FROM phrases WHERE id = ?', (phrase_id,))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
