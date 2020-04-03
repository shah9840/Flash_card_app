import sqlite3

conn = sqlite3.connect('cards.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS stack(
id integer PRIMARY KEY,
question text NOT NULL,
answer text NOT NULL,
deck text NOT NULL,
priority integer,
instance integer)''')

def insert(q,a,d):
    c.execute('''INSERT INTO stack (question,answer,deck,priority,instance) VALUES (?,?,?,?,?)''',[q,a,d,0,0])
    conn.commit()

def fetch():
    cur = conn.cursor()
    cur.execute("SELECT deck FROM stack")
 
    rows = cur.fetchall()
    rows = list(dict.fromkeys(rows))
    return rows

