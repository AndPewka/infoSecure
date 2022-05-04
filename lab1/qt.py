from tkinter import *
from test import *
mask = ""
def clickEncrypt():
    global mask
    word = input1.get()
    b = int(inputa.get())
    a = int(inputb.get())
    if a*b < len(word):
        input2.delete(0,END)
        input2.insert(0,"решетка меньше слова")
        return 

    mask = genMask(word,a,b)
    wordEncr = encrypt(mask,word,a,b)
    input2.delete(0,END)
    input2.insert(0,wordEncr)

def clickDeEncrypt():
    global mask
    word = input1.get()
    word = deEncrypt(mask,word)
    input2.delete(0,END)
    input2.insert(0,word)




window = Tk() 

lbla = Label(window, text="N строк решетки")
lblb = Label(window, text="N столбцов решетки") 

inputa = Entry(window, width=10,font="Monospace 12")
inputa.grid(column=1, row=0)

inputb = Entry(window, width=10,font="Monospace 12")
inputb.grid(column=1, row=1)

lbla.grid(column=0, row=0)  
lblb.grid(column=0, row=1)  

input1 = Entry(window, width=100,font="Monospace 12")
input1.grid(column=0, row=2,columnspan=2)  

btn1 = Button(window, text="Зашифровать", command=clickEncrypt)  
btn1.grid(column=0, row=3)  

btn2 = Button(window, text="Расшифровать", command=clickDeEncrypt)  
btn2.grid(column=1, row=3)

input2 = Entry(window, width=100,font="Monospace 12")
input2.grid(column=0, row=5,columnspan=2,)  



window.mainloop()
