from tkinter import *
from tkinter import messagebox
count=0
def Change(button,boardValRow,boardValCol):
    global count
    if button["text"]=="":
        if count%2==0:
            button["text"]="X"
            l1=Label(t,text="PLAYER:2",height=3,font=("",10,"bold"),bg="white").grid(row=0,column=0)
            board[boardValRow][boardValCol]="X"
        else:
            button["text"]="O"
            l1=Label(t,text="PLAYER:1",height=3,font=("",10,"bold"),bg="white").grid(row=0,column=0)
            board[boardValRow][boardValCol]="O"
        count=count+1
        if count>=5:
            checkWinner()
    else:
        messagebox.showerror("Error","Box filled")
def checkWinner():
    global count,board
    if (board[0][0]==board[0][1]==board[0][2]=="X" or board[1][0]==board[1][1]==board[1][2]=="X" or board[2][0]==board[2][1]==board[2][2]=="X" or board[0][0]==board[1][0]==board[2][0]=="X" or board[0][1]==board[1][1]==board[2][1]=="X" or board[0][2]==board[1][2]==board[2][2]=="X" or board[0][0]==board[1][1]==board[2][2]=="X" or board[0][2]==board[1][1]==board[2][0]=="X"):
            displayWinner("Player X")
    elif (board[0][0]==board[0][1]==board[0][2]=="O" or board[1][0]==board[1][1]==board[1][2]=="O" or board[2][0]==board[2][1]==board[2][2]=="O" or board[0][0]==board[1][0]==board[2][0]=="O" or board[0][1]==board[1][1]==board[2][1]=="O" or board[0][2]==board[1][2]==board[2][2]=="O" or board[0][0]==board[1][1]==board[2][2]=="O" or board[0][2]==board[1][1]==board[2][0]=="O"):
            displayWinner("Player O")
    elif count==9:
        displayWinner("tie")
def displayWinner(win):
    global t,winner
    winner=Tk()
    winner.title("Winner")
    winner.configure(bg="Cyan")
    l1=Label(winner,text="THE WINNER IS: ",bg="Black",fg="White")
    l1.pack()
    l2=Label(winner,text=win,bg="Black",fg="White")
    l2.pack()
    bp=Button(winner,text="OK",command=destruct)
    bp.pack()
def destruct():
 global t,winner
 t.destroy()
 winner.destroy()
def Quit():
 global t 
 msg=messagebox.askquestion("Confirm","Quit?")
 if msg=='yes':
    t.destroy()
board=[["","","",],["","","",],["","","",]]
t=Tk()
t.title("TIC TAC TOE")
t.configure(bg="white")  
l1=Label(t,text="PLAYER:1",height=3,font=("",10,"bold"),bg="white")
l1.grid(row=0,column=0)
exitButton=Button(t,text="Quit",font=("",10,"bold"),command=Quit)
exitButton.grid(row=0,column=2)
b1=Button(t,text="",height=5,width=8,bg="black",activebackground="white",fg="white",command=lambda: Change(b1,0,0))
b1.grid(row=2,column=0)
b2=Button(t,text="",height=5,width=8,bg="black",activebackground="white",fg="white",command=lambda: Change(b2,0,1))
b2.grid(row=2,column=1)
b3=Button(t,text="",height=5,width=8,bg="black",activebackground="white",fg="white",command=lambda: Change(b3,0,2))
b3.grid(row=2,column=2)
b4=Button(t,text="",height=5,width=8,bg="black",activebackground="white",fg="white",command=lambda: Change(b4,1,0))
b4.grid(row=3,column=0)
b5=Button(t,text="",height=5,width=8,bg="black",activebackground="white",fg="white",command=lambda: Change(b5,1,1))
b5.grid(row=3,column=1)
b6=Button(t,text="",height=5,width=8,bg="black",activebackground="white",fg="white",command=lambda: Change(b6,1,2))
b6.grid(row=3,column=2)
b7=Button(t,text="",height=5,width=8,bg="black",activebackground="white",fg="white",command=lambda: Change(b7,2,0))
b7.grid(row=4,column=0)
b8=Button(t,text="",height=5,width=8,bg="black",activebackground="white",fg="white",command=lambda: Change(b8,2,1))
b8.grid(row=4,column=1)
b9=Button(t,text="",height=5,width=8,bg="black",activebackground="white",fg="white",command=lambda: Change(b9,2,2))
b9.grid(row=4,column=2)
t.mainloop()