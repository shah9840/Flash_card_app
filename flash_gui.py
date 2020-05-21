import tkinter as tk
from tkinter import font
import database

q, a = database.fetch_prio()

root = tk.Tk()
canvas = tk.Canvas(root, height=720, width=1280, bg='white')
canvas.pack()
backimg = tk.PhotoImage(file='nature.png')
backlabel = tk.Label(root, image=backimg)
backlabel.place(relwidth=1, relheight=1)



def createdeck():
    decklist = database.fetch()
    backimg = tk.PhotoImage(file='nature.png')
    backlabel = tk.Label(root, image=backimg)
    backlabel.place(relwidth=1, relheight=1)
    # frame = tk.Frame(root, bg='blue', bd=4)
    # frame.place(relheight=0.75, relwidth=0.9, relx=0.5, rely=0.1, anchor='n')

    frame = tk.Frame(root, bg='#7877aa', bd=4)
    frame.place(relheight=0.75, relwidth=0.9, relx=0.5, rely=0.1, anchor='n')
    label = tk.Label(frame, text='Enter Deck Name',
                     font=20, bg='#454bca', fg='white')
    label.place(relwidth=0.2, relheight=0.1, relx=0.1, rely=0.1)
    entry = tk.Entry(frame, bd=2, bg='black', fg='white', font=20)
    entry.place(relwidth=0.4, relheight=0.1, relx=0.33, rely=0.1)
    button = tk.Button(frame, text='Submit', font=20,
                       bg='white', fg='black', command=lambda: deckedit(entry))
    button.place(relx=0.35, rely=0.26, relwidth=0.2, relheight=0.1)
    label = tk.Label(frame, text='Pre Existing decks are:',
                     font=20, bg='purple', fg='red')
    label.place(relwidth=1, relheight=0.1, rely=0.4)
    label = tk.Label(frame, text=decklist, font=20)
    label.place(relwidth=1, relheight=0.35, rely=0.5)
    bt = tk.Button(frame, text="Back", font=20, bg="pink", fg="blue",
                   command=lambda: main())
    bt.place(relx=.75, rely=0.89, relwidth=0.16, relheight=0.1)



def deckedit(entry):
    backimg = tk.PhotoImage(file='nature.png')
    backlabel = tk.Label(root, image=backimg)
    backlabel.place(relwidth=1, relheight=1)
    frame = tk.Frame(root, bg='black', bd=4)
    frame.place(relheight=0.75, relwidth=0.9, relx=0.5, rely=0.1, anchor='n')

    s = entry.get()
    # frame = tk.Frame(root, bg='#eeeeee', bd=4)
    # frame.place(relheight=1, relwidth=1, relx=0.5, rely=0, anchor='n')
    label = tk.Label(frame, text='Deck: '+s, font=20, bg='blue', fg='white')
    label.place(relwidth=0.2, relheight=0.1, rely=0, relx=0.4)
    label = tk.Label(frame, text='Question:', font=24, bg='purple', fg='red')
    label.place(relwidth=1, relheight=0.1, rely=0.15)
    qbox = tk.Entry(frame, bd=2, font=20)
    qbox.place(relwidth=1, relheight=0.2, rely=0.25)
    label = tk.Label(frame, text='Answer:', font=24, bg='purple', fg='white')
    label.place(relwidth=1, relheight=0.1, rely=.50)
    abox = tk.Entry(frame, bd=2, font=20)
    abox.place(relwidth=1, relheight=0.2, rely=.6)
    button = tk.Button(frame, text='Submit', font=20,
                       bg='white', fg='black', command=lambda: inputdata(qbox, abox, entry))
    button.place(relx=0.06, rely=0.889, relwidth=.2, relheight=0.1)
    button = tk.Button(frame, text='Exit', font=18,
                       bg='white', fg='black', command=lambda: main())
    button.place(relx=.75, rely=0.889, relwidth=.2, relheight=0.1)
  

def inputdata(qbox, abox, entry):
    q = qbox.get()
    a = abox.get()
    d = entry.get()
    database.insert(q, a, d)
    deckedit(entry)


def nexttab():
    
    frame = tk.Frame(root, bg='purple', bd=4)
    frame.place(relheight=0.75, relwidth=0.9, relx=0.5, rely=0.1, anchor='n')
    label = tk.Label(frame, font=50, bg='white', fg='black')
    label.place(relwidth=1, relheight=0.7)
    button = tk.Button(frame, text="Very Easy", font=40,
                       bg='white', fg='black', command=lambda: open_deck())
    button.place(relx=0.05, rely=0.75, relwidth=0.20, relheight=0.2)
    button = tk.Button(frame, text="Easy", font=40,
                       bg='white', fg='black', command=lambda: open_deck())
    button.place(relx=0.29, rely=0.75, relwidth=0.20, relheight=0.2)
    button = tk.Button(frame, text="Medium", font=40,
                       bg='white', fg='black', command=lambda: open_deck())
    button.place(relx=0.53, rely=0.75, relwidth=0.20, relheight=0.2)
    button = tk.Button(frame, text="Hard", font=40,
                       bg='white', fg='black', command=lambda: open_deck())
    button.place(relx=0.78, rely=0.75, relwidth=0.20, relheight=0.2)
    
    label.config(font=("Courier", 44))
    try:
        answer = a.pop()
        label['text'] = answer
    except:
        label['text'] = "answer not found"



def open_deck():

    canvas = tk.Canvas(root, height=720, width=1280, bg='white')
    canvas.pack()
    backimg = tk.PhotoImage(file='nature.png')
    backlabel = tk.Label(root, image=backimg)
    backlabel.place(relwidth=1, relheight=1)
    frame = tk.Frame(root, bg='blue', bd=4)
    frame.place(relheight=0.75, relwidth=0.9, relx=0.5, rely=0.1, anchor='n')
    label = tk.Label(frame, font=50, bg='white', fg='black')
    label.place(relwidth=1, relheight=0.7)
    label.config(font=("Courier", 44))
    
    try:
        question = q.pop()
        label['text'] = question
    except:
        label['text'] = "question not found"
    button = tk.Button(frame, text="Show Answer", font=40,
                       bg='white', fg='black', command=lambda: nexttab())
    button.place(relx=0.35, rely=0.75, relwidth=0.3, relheight=0.2)
    bt = tk.Button(frame, text="Back", font=20, bg="pink", fg="blue", 
                command=lambda: main())
    bt.place(relx=.75, rely=0.85, relwidth=0.16, relheight=0.1)
    root.mainloop()


def main():
    decklist = database.fetch()
    backimg = tk.PhotoImage(file='nature.png')
    backlabel = tk.Label(root, image=backimg)
    backlabel.place(relwidth=1, relheight=1)

    deckframe = tk.Frame(root, bg='purple', bd=4)
    deckframe.place(relheight=0.75, relwidth=0.9,
                    relx=0.5, rely=0.1, anchor='n')
    decklabel = tk.Label(deckframe,  bg='black', fg='white')
    decklabel.place(relwidth=1, relheight=0.1)
    decklabel.config(font=("Courier", 28))
    decklabel['text'] = "Decks"
    space = 0.05
    for x in decklist:
        button = tk.Button(deckframe, text=x, font=18,
                           bg='white', fg='black', command=lambda: open_deck())
        button.place(relx=0.3, rely=0.111+space, relwidth=0.4, relheight=0.1)
        space = space+0.1
    button = tk.Button(deckframe, text='Edit deck', font=18,
                       bg='blue', fg='black', command=lambda: createdeck())
    button.place(relx=0.05, rely=0.85, relwidth=0.2, relheight=0.1)
    button = tk.Button(deckframe, text='Quit Program', font=18,
                       bg='red', fg='black', command=lambda: quit())
    button.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.1)

    root.mainloop()


def quit():
    database.conn.close()
    root.quit()
    exit()


# if __name__ == "__main__":
#     main()

def intro():
    backimg = tk.PhotoImage(file='nature.png')
    backlabel = tk.Label(root, image=backimg)
    backlabel.place(relwidth=1, relheight=1)
    button = tk.Button(root, text="Start", font=80,
                       bg='purple', fg='white', command=lambda: main())
    button.place(relx=0.55, rely=0.4, relwidth=0.2, relheight=0.1)
    label = tk.Label(root, font=50, bg='#caf766', fg='green')
    label.place(relwidth=0.45, relheight=0.18, relx=0.5, rely=0.2)
    label.config(font=("Courier", 40))
    label['text'] = "Flash Card World"

    
    root.mainloop()

intro()







