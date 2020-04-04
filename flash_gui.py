import tkinter as tk
from tkinter import font
import database


root = tk.Tk()

def createdeck():
    decklist=database.fetch()
    frame = tk.Frame(root, bg='#eeeeee', bd=4)
    frame.place(relheight=1, relwidth=1, relx=0.5, rely=0, anchor='n')
    label = tk.Label(frame,text='Enter Deck Name',font=18)
    label.place(relwidth=.3, relheight=0.05)
    entry = tk.Entry(frame,bd=5)
    entry.place(relwidth=.7,relheight=0.05,relx=.31)
    button = tk.Button(frame, text='Submit', font=18,
                       bg='white', fg='black', command=lambda: deckedit(entry))
    button.place(relx=0,rely=0.05, relwidth=1, relheight=0.05)
    label = tk.Label(frame,text='Pre Existing decks are:',font=18)
    label.place(relwidth=1, relheight=0.05,rely=.5)
    label = tk.Label(frame,text=decklist,font=18)
    label.place(relwidth=1, relheight=0.05,rely=.55)

def deckedit(entry):
    s=entry.get()
    frame = tk.Frame(root, bg='#eeeeee', bd=4)
    frame.place(relheight=1, relwidth=1, relx=0.5, rely=0, anchor='n')
    label = tk.Label(frame,text='Deck:'+s,font=18)
    label.place(relwidth=1, relheight=0.05)
    label = tk.Label(frame,text='Question:',font=18)
    label.place(relwidth=1, relheight=0.05,rely=.05)
    qbox = tk.Entry(frame,bd=5)
    qbox.place(relwidth=1,relheight=0.3,rely=.1)
    label = tk.Label(frame,text='Answer:',font=18)
    label.place(relwidth=1, relheight=0.05,rely=.45)
    abox = tk.Entry(frame,bd=5)
    abox.place(relwidth=1,relheight=0.3,rely=.5)
    button= tk.Button(frame,text='Submit',font=18,
                      bg='white',fg='black',command=lambda:inputdata(qbox,abox,entry))
    button.place(relx=0,rely=0.889,relwidth=.5,relheight=0.05)
    button= tk.Button(frame,text='Exit',font=18,
                      bg='white',fg='black',command=lambda:main())
    button.place(relx=.5,rely=0.889,relwidth=.5,relheight=0.05)

def inputdata(qbox,abox,entry):
    q=qbox.get()
    a=abox.get()
    d=entry.get()
    database.insert(q,a,d)
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
    ans = "Answer"
    label.config(font=("Courier", 44))
    label['text'] = ans


def open_deck():
    canvas = tk.Canvas(root, height=720, width=1280 , bg = 'white')
    canvas.pack()
    backimg = tk.PhotoImage(file='nature.png')
    backlabel = tk.Label(root, image=backimg)
    backlabel.place(relwidth=1, relheight=1)
    frame = tk.Frame(root, bg='blue', bd=4)
    frame.place(relheight=0.75, relwidth=0.9, relx=0.5, rely=0.1, anchor='n')
    label = tk.Label(frame, font=50, bg='white', fg='black')
    label.place(relwidth=1, relheight=0.7)
    label.config(font=("Courier", 44))
    label['text'] = "Question"
    button = tk.Button(frame, text="Show Answer", font=40,
                       bg='white', fg='black', command=lambda: nexttab())
    button.place(relx=0.35,rely=0.75, relwidth=0.3, relheight=0.2)
    root.mainloop()

def main():
    decklist = database.fetch()
    deckframe = tk.Frame(root, bg='#eeeeee', bd=4)
    deckframe.place(relheight=1, relwidth=1, relx=0.5, rely=0, anchor='n')
    decklabel = tk.Label(deckframe,  bg='white', fg='black')
    decklabel.place(relwidth=1, relheight=0.1)
    decklabel.config(font=("Courier",28))
    decklabel['text']="Decks"
    space = 0
    for x in decklist:
        button = tk.Button(deckframe, text=x, font=18,
                           bg='white', fg='black', command=lambda: open_deck())
        button.place(relx=0,rely=0.111+space, relwidth=1, relheight=0.05)
        space = space+0.05
    button= tk.Button(deckframe,text='Edit deck',font=18,
                        bg='white',fg='black',command=lambda:createdeck())
    button.place(relx=0,rely=0.778,relwidth=1,relheight=0.05)
    button= tk.Button(deckframe,text='Quit Program',font=18,
                      bg='white',fg='black',command=lambda:quit())
    button.place(relx=0,rely=0.889,relwidth=1,relheight=0.05)
    root.mainloop()

def quit():
    database.conn.close()
    root.quit()

if __name__ == "__main__":
    main()
