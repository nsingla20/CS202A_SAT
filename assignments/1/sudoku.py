from tkinter import *
import random
numbers = [1,2,3,4,5,6,7,8,9]
window=Tk()
window.title("SUDOKO")
def reg():
    def makeBoard():
         board = None
         while board is None:
         board = attemptBoard()
         return board

def attemptBoard():
    board = [[None for  in range(9)] for  in range(9)]
    for i in range(9):
        for j in range(9):
            checking = numbers[:]
            random.shuffle(checking)
            x = -1
            loopStart = 0
            while board[i][j] is None:
                x += 1
                if x == 9:

                    return None
                checkMe = [checking[x],True]
                if checkMe in board[i]:

                    continue
                checkis = False
                for checkRow in board:
                    if checkRow[j] == checkMe:

                        checkis = True
                if checkis: continue

                if i % 3 == 1:
                    if   j % 3 == 0 and checkMe in (board[i-1][j+1],board[i-1][j+2]): continue
                    elif j % 3 == 1 and checkMe in (board[i-1][j-1],board[i-1][j+1]): continue
                    elif j % 3 == 2 and checkMe in (board[i-1][j-1],board[i-1][j-2]): continue
                elif i % 3 == 2:
                    if   j % 3 == 0 and checkMe in (board[i-1][j+1],board[i-1][j+2],board[i-2][j+1],board[i-2][j+2]): continue
                    elif j % 3 == 1 and checkMe in (board[i-1][j-1],board[i-1][j+1],board[i-2][j-1],board[i-2][j+1]): continue
                    elif j % 3 == 2 and checkMe in (board[i-1][j-1],board[i-1][j-2],board[i-2][j-1],board[i-2][j-2]): continue

                board[i][j] = checkMe
    return board
a=makeBoard()
rows = []
for i in range(1,10):
    cols = []
    for j in range(1,10):
        e = Label(window,text=str(a[i-1][j-1][0]),width=6, relief="groove")
        e.grid(row=i, column=j, sticky=NSEW,)
        cols.append(e)
    rows.append(cols)
l1=Label(window,text="*")
l1.grid(row=0,column=0)
l2=Label(window,text="9*9 SUDOKU Generator",height=3)
l2.grid(row=0,column=3,columnspan=4)

b1=Button(window,text="Regenerate",width=6,command=reg)
b1.grid(row=10,column=8)
b6=Button(window,text="close",width=6,command=window.destroy)
b6.grid(row=11,column=8)

reg()
window.mainloop()