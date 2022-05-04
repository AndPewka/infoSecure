from tkinter import *
import json
from rsaLib import *

e = ""
d = ""
n = ""
def clickEncrypt():
    global e,d,n
    e,n,d = getKeys()
    message = inputa.get("1.0", "end-1c")
    enc = encrypt(e,n,message)
    inputb.delete("1.0", "end-1c")
    inputb.insert("1.0", str(enc))

def clickGen():
    global e,n,d
    e,n,d = generateKeys(53)

    input1.delete(0,END)
    input1.insert(0,str((e,n)))

    input2.delete(0,END)
    input2.insert(0,str((d,n)))

    return e,n,d


def clickDeEncrypt():
    global e,n,d
    e,n,d = getKeys()
    message = inputa.get("1.0", "end-1c")
    try:
        decr = decrypt(d,n,message)
    except:
        errorUP("fix private key")
        return
    inputb.delete("1.0", "end-1c")
    inputb.insert("1.0", str(decr))

def getKeys():
    publicKey = input1.get()
    privateKey = input2.get()
    if publicKey:
        publicKey = publicKey.replace("(","[")
        publicKey = json.loads(publicKey.replace(")","]"))
    if privateKey:
        privateKey = privateKey.replace("(","[")
        privateKey = json.loads(privateKey.replace(")","]"))

    e = publicKey[0]
    d = privateKey[0]
    n = privateKey[1]


    return e,n,d

def errorUP(message):
    inputb.delete("1.0", "end-1c")
    inputb.insert("1.0", message)

window = Tk() 

lbla = Label(window, text="Public key")

lblb = Label(window, text="Private key") 

inputa = Text(width=80, height=10, font = "Monospace 12")
inputa.grid(column=0, row=0,columnspan=3)


inputb = Text(width=80, height=10, font = "Monospace 12")
inputb.grid(column=0, row=1,columnspan=3)


lbla.grid(column=0, row=2,columnspan=3)  
lblb.grid(column=0, row=4,columnspan=3)  

input1 = Entry(window, width=160,font="Monospace 12")
input1.grid(column=0, row=3,columnspan=3)  

input2 = Entry(window, width=160,font="Monospace 12")
input2.grid(column=0, row=5,columnspan=3)  



btn1 = Button(window, text="Зашифровать", command=clickEncrypt)  
btn1.grid(column=0, row=6)  

btn2 = Button(window, text="Сгенирировать ключи", command=clickGen)  
btn2.grid(column=1, row=6)

btn3 = Button(window, text="Расшифровать", command=clickDeEncrypt)  
btn3.grid(column=2, row=6)


e,n,d = clickGen()
window.mainloop()


