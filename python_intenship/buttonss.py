# from tkinter import *

# root = Tk()
# root.title("PythonLobby")
# w = Label(root,text='Python.com',font="60")
# w.pack()

# Checkbox1 = IntVar()
# Checkbox2 = IntVar()

# Button0 = Checkbutton(root,text="Learning",
#                       variable=Checkbox1,
#                       onvalue = 1,
#                       offvalue = 0,
#                       height =3,
#                       width=12)
# Button1=Checkbutton(root,text="Tutorial",
#                     variable=Checkbox2 ,
#                     onvalue = 1,
#                     offvalue = 0,
#                     height =3,
#                     width = 12)

# Button0.pack()
# Button1.pack()

# root.geometry("320x220")
# root.mainloop()

from tkinter import *

root = Tk()
root.title("PythonLobby")

value1 = StringVar(root,"2")

rbtn1 = Radiobutton(root,text="Radiobutton1",variable=value1,value="1")
rbtn1.pack()
rbtn2 = Radiobutton(root,text="Radiobutton2",variable=value1,value="2")
rbtn2.pack()
rbtn3 = Radiobutton(root,text="Radiobutton3",variable=value1,value="3")
rbtn3.pack()

root.geometry("250x200")
mainloop()