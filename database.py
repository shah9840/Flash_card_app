import sqlite3

conn = sqlite3.connect('cards.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS stack(
id integer PRIMARY KEY,
question text NOT NULL,
answer text NOT NULL,
deck text NOT NULL,
priority integer)''')

def insert():
    i=0
    for i in range(1,20):
        print('question:')
        question = input()
        print('answer:')
        answer = input()
        print('deck:')
        deck= input()
        c.execute('''INSERT INTO stack (question,answer,deck,priority) VALUES (?,?,?,?)''',[question,answer,deck,0])
        i=i+1
    conn.commit()
    conn.close()

def fetch():
    cur = conn.cursor()
    cur.execute("SELECT deck FROM stack")
 
    rows = cur.fetchall()
    rows = list(dict.fromkeys(rows))
    return rows
