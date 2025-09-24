import sqlite3

# Connetti al database (se non esiste, viene creato)
conn = sqlite3.connect('backend/database.db')
c = conn.cursor()

# Crea una tabella (esempio: utenti)
c.execute('''
CREATE TABLE IF NOT EXISTS phrases (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    phrase TEXT NOT NULL
)
''')

conn.commit()
conn.close()
print("Database creato!")
