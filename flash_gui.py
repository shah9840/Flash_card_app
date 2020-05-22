import tkinter as tk
from tkinter import font
import database

cardfontsize=22
fontype = "Courier"
backimage= "1366x768.png"
foreground = "#F8F8F2"
background = "#282A36"
bannerred = "#FF5555"
bannergreen = "#50fa7b"
banneryellow = "#f1fa8c"
bannerpurple = "#bd93f9"
bannergrey = "#bfbfbf"
bannerblue = "#8be9fd"


root = tk.Tk()
canvas = tk.Canvas(root, height=768, width=1366, bg='white')
canvas.pack()
backimg = tk.PhotoImage(file=backimage)
backlabel = tk.Label(root, image=backimg)
backlabel.place(relwidth=1, relheight=1)



def createdeck():
    decklist = database.fetch_deck()
    frame = tk.Frame(root, bg=background, bd=4)
    frame.place(relheight=0.75, relwidth=0.9, relx=0.5, rely=0.1, anchor='n')
    label = tk.Label(frame, text='Enter Deck Name',
                     font=20, bg=bannerblue, fg='black')
    label.place(relwidth=0.2, relheight=0.1, relx=0.1, rely=0.1)
    entry = tk.Entry(frame, bd=2, bg=background, fg='white', font=20)
    entry.place(relwidth=0.4, relheight=0.1, relx=0.33, rely=0.1)
    button = tk.Button(frame, text='Submit', font=20,
                       bg=bannergrey, fg='black', command=lambda: deckedit(entry))
    button.place(relx=0.35, rely=0.26, relwidth=0.2, relheight=0.1)
    label = tk.Label(frame, text='Pre Existing decks are:',
                     font=20, bg=bannerpurple, fg='black')
    label.place(relwidth=1, relheight=0.1, rely=0.4)
    label = tk.Label(frame, text=decklist, font=20)
    label.place(relwidth=1, relheight=0.35, rely=0.5)
    bt = tk.Button(frame, text="Back", font=20, bg=bannerred, fg="black",
                   command=lambda: maindeck())
    bt.place(relx=.75, rely=0.89, relwidth=0.16, relheight=0.1)



def deckedit(entry):
    s = entry.get()
    frame = tk.Frame(root, bg=bannergrey, bd=4)
    frame.place(relheight=0.75, relwidth=0.9, relx=0.5, rely=0.1, anchor='n')
    label = tk.Label(frame, text='Deck: '+s, font=20, bg=background, fg=foreground)
    label.place(relwidth=0.2, relheight=0.1, rely=0, relx=0.4)
    label = tk.Label(frame, text='Question:', font=24, bg=bannerpurple, fg='black')
    label.place(relwidth=1, relheight=0.1, rely=0.15)
    qbox = tk.Entry(frame, bd=2, font=20)
    qbox.place(relwidth=1, relheight=0.2, rely=0.25)
    label = tk.Label(frame, text='Answer:', font=24, bg=bannerpurple, fg='black')
    label.place(relwidth=1, relheight=0.1, rely=.50)
    abox = tk.Entry(frame, bd=2, font=20)
    abox.place(relwidth=1, relheight=0.2, rely=.6)
    button = tk.Button(frame, text='Submit', font=20,
                       bg=bannergreen, fg='black', command=lambda: inputdata(qbox, abox, entry))
    button.place(relx=0.06, rely=0.889, relwidth=.2, relheight=0.1)
    button = tk.Button(frame, text='Exit', font=18,
                       bg=bannerred, fg='black', command=lambda: maindeck())
    button.place(relx=.75, rely=0.889, relwidth=.2, relheight=0.1)
  

def inputdata(qbox, abox, entry):
    q = qbox.get()
    a = abox.get()
    d = entry.get()
    database.insert(q, a, d)
    deckedit(entry)


def complete(answer, x, deck_name):
    database.prio_update(answer,x)
    # open_deck(id)
    define_deck(deck_name)


def nexttab(number, deck_name):
    column = "answer"
    frame = tk.Frame(root, bg='purple', bd=4)
    frame.place(relheight=0.75, relwidth=0.9, relx=0.5, rely=0.1, anchor='n')
    label = tk.Label(frame, font=50, bg=foreground, fg=background)
    label.place(relwidth=1, relheight=0.7)
    label.config(font=(fontype, cardfontsize))
    label['text'] = database.fetch(number,column)

    button = tk.Button(frame, text="Very Easy", font=40,
                       bg=bannergreen, fg='black', command=lambda: complete(number, 0, deck_name))
    button.place(relx=0.05, rely=0.75, relwidth=0.20, relheight=0.2)
    button = tk.Button(frame, text="Easy", font=40,
                       bg=bannerblue, fg='black', command=lambda: complete(number, 1, deck_name))
    button.place(relx=0.29, rely=0.75, relwidth=0.20, relheight=0.2)
    button = tk.Button(frame, text="Medium", font=40,
                       bg=banneryellow, fg='black', command=lambda: complete(number, 2, deck_name))
    button.place(relx=0.53, rely=0.75, relwidth=0.20, relheight=0.2)
    button = tk.Button(frame, text="Hard", font=40,
                       bg=bannerred, fg='black', command=lambda: complete(number, 3, deck_name))
    button.place(relx=0.78, rely=0.75, relwidth=0.20, relheight=0.2)
    

def define_deck(deck_name):
    global id
    id = database.fetch_id(''.join(deck_name))
    print(id)
    open_deck(id, deck_name)

def open_deck(id, deck_name):
    column = "question"
    frame = tk.Frame(root, bg='violet', bd=4)
    frame.place(relheight=0.75, relwidth=0.9, relx=0.5, rely=0.1, anchor='n')
    label = tk.Label(frame, font=50, bg=background, fg=foreground)
    label.place(relwidth=1, relheight=0.7)
    label.config(font=(fontype, cardfontsize))
    try:
        temp = id.pop()
        number = list(map(int, temp))
        label['text'] = database.fetch(number,column)
    except:
        maindeck()
    button = tk.Button(frame, text="Show Answer", font=40,
                       bg=background, fg=foreground, command=lambda: nexttab(number, deck_name))
    button.place(relx=0.35, rely=0.75, relwidth=0.3, relheight=0.2)
    bt = tk.Button(frame, text="Back", font=20, bg=bannerred, fg="black",
                command=lambda: maindeck())
    bt.place(relx=.75, rely=0.85, relwidth=0.16, relheight=0.1)
    root.mainloop()


def maindeck():
    decklist = database.fetch_deck()

    deckframe = tk.Frame(root, bg=background, bd=4)
    deckframe.place(relheight=0.75, relwidth=0.9,
                    relx=0.5, rely=0.1, anchor='n')
    decklabel = tk.Label(deckframe,  bg='#4afdaf', fg='black')
    decklabel.place(relwidth=1, relheight=0.1)
    decklabel.config(font=(fontype, 28))
    decklabel['text'] = "Decks"
    space = 0.05
    for i in decklist:
        button = tk.Button(deckframe, text=i, font=18,
                           bg='violet', fg="black", command=lambda i=i:define_deck(i))
        button.place(relx=0.3, rely=0.111+space, relwidth=0.4, relheight=0.1)
        space = space+0.1
    button = tk.Button(deckframe, text='Edit deck', font=18,
                       bg=bannerblue, fg='black', command=lambda: createdeck())
    button.place(relx=0.05, rely=0.85, relwidth=0.2, relheight=0.1)
    button = tk.Button(deckframe, text='Quit Program', font=18,
                       bg=bannerred, fg='black', command=lambda: quit())
    button.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.1)

    button = tk.Button(deckframe, text='Reset', font=18,
                       bg=bannerred, fg='black', command=lambda: database.reset_prio())
    button.place(relx=0.5, rely=0.85, relwidth=0.2, relheight=0.1)

    root.mainloop()


def quit():
    database.conn.close()
    root.quit()
    exit()



def main():
    button = tk.Button(root, text="Start", font=80,
                       bg=background, fg=foreground, command=lambda: maindeck())
    button.place(relx=0.2, rely=0.4, relwidth=0.2, relheight=0.1)
    label = tk.Label(root, font=50, bg=background, fg=foreground)
    label.place(relwidth=0.4, relheight=0.18, relx=0.2, rely=0.2)
    label.config(font=(fontype, 40))
    label['text'] = "Flash Card World"

    
    root.mainloop()

if __name__ == "__main__":
     main()


