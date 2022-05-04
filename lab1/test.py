from random import randint,choice

def genMask(word,a,b):
    mask = []
    symbCount = a*b
    while len(mask) < len(word):
        addMask = randint(0,symbCount-1)
        if addMask not in mask:
            mask.append(addMask)

    print(mask)
    return mask

def encrypt(mask,word,a,b):
    grid = []

    for i in range(a*b):
        grid.append("")

    for i in range(len(mask)):
        grid[mask[i]] = word[i]

    symbols = "qwertyuiopasdfghjklzxcvbnm1234567890"

    for i in range(len(grid)):
        if grid[i]=="":
            grid[i]= choice(list(symbols))

    gridWord = "".join(grid)

    return gridWord

def deEncrypt(mask,encryptWord):
    massive = []
    for i in mask:
        massive.append(encryptWord[i])

    return "".join(massive)
