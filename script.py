from tkinter import *


root = Tk()
root.title("Title")
root.geometry("640x480")


label = Label(text =u'aiueo')
label.pack()
text_field = Entry()
text_field.pack()
Button = Button(text=u'Compile')
Button.bind("<Button-1>",compile)
Button.pack()

def compile():
    value = text_field.get()
    print(value)
    lab = LAbel(value)
root.mainloop()
