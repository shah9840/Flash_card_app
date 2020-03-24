import tkinter as tk
from tkinter import font


root = tk.Tk()
canvas = tk.Canvas(root, height=600, width = 600, bg = 'white')
canvas.pack()
backimg = tk.PhotoImage(file='nature.png')
backlabel = tk.Label(root, image=backimg)
backlabel.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg='blue', bd=4)
frame.place(relheight=0.75, relwidth=0.9, relx=0.5, rely=0.1, anchor='n')
label = tk.Label(frame, font=50, bg='white', fg='black')
label.place(relwidth=1, relheight=0.7)


def nexttab():
    frame = tk.Frame(root, bg='purple', bd=4)
    frame.place(relheight=0.75, relwidth=0.9, relx=0.5, rely=0.1, anchor='n')
    label = tk.Label(frame, font=50, bg='white', fg='black')
    label.place(relwidth=1, relheight=0.7)


    button = tk.Button(frame, text="Very Easy", font=40,
                    bg='white', fg='black', command=lambda: main())
    button.place(relx=0.05, rely=0.75, relwidth=0.20, relheight=0.2)
    
    button = tk.Button(frame, text="Easy", font=40,
                       bg='white', fg='black', command=lambda: main())
    button.place(relx=0.29, rely=0.75, relwidth=0.20, relheight=0.2)
    
    button = tk.Button(frame, text="Medium", font=40,
                       bg='white', fg='black', command=lambda: main())
    button.place(relx=0.53, rely=0.75, relwidth=0.20, relheight=0.2)
    
    button = tk.Button(frame, text="Hard", font=40,
                       bg='white', fg='black', command=lambda: main())
    button.place(relx=0.78, rely=0.75, relwidth=0.20, relheight=0.2)
    ans = "Answer"
    label.config(font=("Courier", 44))

    label['text'] = ans
    

def start():
    main()

def func():
    nexttab()
        
def main():
    label.config(font=("Courier", 44))
    label['text'] = "Question"

    button = tk.Button(frame, text="Show Answer", font=40,
                    bg='white', fg='black', command=lambda: func())
    button.place(relx=0.35,rely=0.75, relwidth=0.3, relheight=0.2)
    root.mainloop()


main()
