import sqlite3

conn = sqlite3.connect('cards.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS stack(
id integer PRIMARY KEY,
question text NOT NULL,
answer text NOT NULL,
deck text NOT NULL, 
priority integer)''')

def insert(q,a,d):
    c.execute('''INSERT INTO stack (question,answer,deck,priority) VALUES (?,?,?,?)''',[q,a,d,3])
    conn.commit()

def fetch(number,column):
    # number = id number,   column = question
    cur = conn.cursor()
    values = ','.join([str(i) for i in number])
    # print(values)
    if column == "question":
        cur.execute('''SELECT question FROM stack WHERE id = ?''',(values))
    else:
        cur.execute('''SELECT answer FROM stack WHERE id = ? ''',[values])

    rows = cur.fetchall()
    # print(rows)
    return rows


def fetch_deck():
    cur = conn.cursor()
    cur.execute("SELECT deck FROM stack")
 
    rows = cur.fetchall()
    rows = list(dict.fromkeys(rows))
    return rows


def fetch_id(x):
    cur = conn.cursor()
    cur.execute('''SELECT id FROM stack WHERE priority != 0 and deck LIKE ? ORDER BY priority ASC;''',[x])
    # sorts the ids in increasing oredr of priority
    id = cur.fetchall()
    # print(id)
    return id


def reset_prio():
    cur = conn.cursor()
    
    cur.execute('''UPDATE stack SET priority = ? ''',[3])
    conn.commit()
    
    
def prio_update(number, x):
    cur = conn.cursor()

    values = ','.join([str(i) for i in number])
    cur.execute('''UPDATE stack SET priority = ? WHERE id=?''', [x, values])
    conn.commit()
    
# fetch_id("chem")
reset_prio()