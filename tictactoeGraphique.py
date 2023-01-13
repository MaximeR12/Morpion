import tkinter as tk

signe='X'
morpion = tk.Tk()
content= [ ['1',' ',' '] , ['2',' ',' '] , ['3',' ',' '] ]

def reset_plateau():
    for i in range(3):
        for j in range(3):
            l[i][j]=' '

def afficher_plateau():
    global signe
    for i in range(3):
        for j in range(3):
            bgrid[i][j] = tk.Button(
                master = morpion,
                background='light gray',
                relief=tk.FLAT,
                borderwidth= 5,
                command=lambda x = i*3+j : changer_signe(x)

            )
            bgrid[i][j].grid(row = i, column = j)



def changer_signe(x):
    global signe
    sign_list[x-1]=signe
    

    pass
bgrid=[
    ['','',''],
    ['','',''],
    ['','','']
]

sign_list=[
    [' ',' ',' ',
    ' ',' ',' ',
    ' ',' ',' ']
]
tk.TkVersion  


afficher_plateau()
bgrid[1][1].configure(text='X')

morpion.mainloop()