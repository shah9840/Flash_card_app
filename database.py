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
    c.execute('''INSERT INTO stack (question,answer,deck,priority,instance) VALUES (?,?,?,?,?)''',[q,a,d,3,0])
    conn.commit()

def fetch():
    cur = conn.cursor()
    cur.execute("SELECT deck FROM stack")
 
    rows = cur.fetchall()
    rows = list(dict.fromkeys(rows))
    return rows


def fetch_prio():
    cur = conn.cursor()
    cur.execute("SELECT question, answer, id FROM stack WHERE priority = 3")

    rows = cur.fetchall()

    q = []
    a = []
    i = []
    for i in range(len(rows)):
        q.append(rows[i][0])
        a.append(rows[i][1])
        # i.append(rows[i][2])

    return q, a
