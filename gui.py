from tkinter import *
from tkinter import ttk

# root = Tk()
inp = ["", ""]
inpRow = 0
inpCol = 0
temp_board = []


def submit_inp(event):
    # print('abc')
    global inp
    if temp_board[inp]
    inp[0] = str(inpRow.get())
    inp[1] = str(inpCol.get())
    print(inp)


def gameWindow(board, size):
    root = Tk()
    global inpCol, inpRow, temp_board
    board = [['x', 'x', ' '], ['o', 'x', 'o'], ['x', ' ', 'x']]
    temp_board = board
    text1 = ['1 ', board[0][0], '|', board[0][1], '|', board[0][2]]
    text1 = ' '.join(text1)
    text2 = ['2 ', board[1][0], '|', board[1][1], '|', board[1][2]]
    text2 = ' '.join(text2)
    text3 = ['3 ', board[2][0], '|', board[2][1], '|', board[2][2]]
    text3 = ' '.join(text3)
    """Label(root, text=' 0  A   B   C').grid(row=0, pady=0)
    Label(root, text=text1).grid(row=1, pady=0)
    Label(root, text='    __|__|___').grid(row=2, pady=0)
    Label(root, text=text2).grid(row=3, pady=0)
    Label(root, text='    __|__|___').grid(row=4, pady=0)
    Label(root, text=text3).grid(row=5, pady=0)
    Label(root, text='      |   |   ').grid(row=6, pady=0)"""
    Label(root, text='  0  A   B   C').pack()
    Label(root, text=text1).pack()
    Label(root, text='      __|__|___').pack()
    Label(root, text=text2).pack()
    Label(root, text='      __|__|___').pack()
    Label(root, text=text3).pack()
    Label(root, text='       |   |   ').pack()
    inpRow = Entry(root)
    inpRow.pack()
    inpCol = Entry(root)
    inpCol.pack()
    subButton = Button(root, text='submit')
    subButton.bind("<Button-1>", submit_inp)
    subButton.pack()
    root.mainloop()

gameWindow(0, 0)
