# from tkinter import *

# root=Tk()
# root.mainloop()

# from tkinter import *

# root = Tk()
# root.title("Welcome to python lobby")
# root.geometry('300x200')

# root,mainloop()

# from tkinter import *

# root = Tk()

# root.title("Welcome to Python Lobby")
# root.geometry('250x200')

# Ibl = Label(root,text = "We are Python Lobby-ian",font=("Halvetica",12),fg='white',bg='black')
# Ibl.pack()

# root.mainloop()

# from tkinter import *

# root = Tk()
# root.title("Welcome to Python Lobby")

# def clicked():
#     print("I am clicked")
# btn = Button(root,text="click me", command = clicked)
# btn.pack()
# root.geometry('250x200')
# root.mainloop()

# from tkinter import *

# root = Tk()
# root.title("Welcome to Python Lobby")

# entry = Entry(root,bg='yellow',fg='red',bd=5)
# entry.place(x=200,y=200)

# root.geometry('250x200')
# root.mainloop()

from tkinter import *

root = Tk()
root.title("Welcome to Instagram")
root.geometry('250x200')

Ibl1 = Label(root,text="Instagram")
Ibl1.pack()

Ibl2 = Label(root,text="Username")
Ibl2.pack()

entry1 = Entry(root,bg='white',fg='black',bd=5)
entry1.pack()

Ibl3 = Label(root,text="Password")
Ibl3.pack()

entry2 = Entry(root,bg='white',fg='black',bd=5)
entry2.pack()

def clicked():
    print("successfuly login")
btn = Button(root,text="Log in",command=clicked)
btn.place(x=660,y=120)





root.mainloop()

