import tkinter as tk
import random
from PIL import ImageTk,Image
root=tk.Tk()
root.geometry("900x640")
root.title("Tik-tac-toe")
root.configure(bg='#a5ccb0')
def set_board():
    global cells
    global img
    img=Image.open("images/cover.png")
    img=img.resize((215,215))
    img=ImageTk.PhotoImage(img)
    b1=tk.Button(root,image=img,height=195,width=190,bg='white',command=lambda:set_coin(1))
    b1.grid(row=0,column=0)
    b2=tk.Button(root,image=img,height=195,width=190,bg='white',command=lambda:set_coin(2))
    b2.grid(row=0,column=1)
    b3=tk.Button(root,image=img,height=195,width=190,bg='white',command=lambda:set_coin(3))
    b3.grid(row=0,column=2)
    b4=tk.Button(root,image=img,height=195,width=190,bg='white',command=lambda:set_coin(4))
    b4.grid(row=1,column=0)
    b5=tk.Button(root,image=img,height=195,width=190,bg='white',command=lambda:set_coin(5))
    b5.grid(row=1,column=1)
    b6=tk.Button(root,image=img,height=195,width=190,bg='white',command=lambda:set_coin(6))
    b6.grid(row=1,column=2)
    b7=tk.Button(root,image=img,height=195,width=190,bg='white',command=lambda:set_coin(7))
    b7.grid(row=2,column=0)
    b8=tk.Button(root,image=img,height=195,width=190,bg='white',command=lambda:set_coin(8))
    b8.grid(row=2,column=1)
    b9=tk.Button(root,image=img,height=195,width=190,bg='white',command=lambda:set_coin(9))
    b9.grid(row=2,column=2)
    cells=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
    b10=tk.Button(root,text="EXIT",height=2,activebackground="lightgrey",width=15,bg='red',font={25,'bold','cursive'},command=root.destroy)
    b10.place(x=700,y=100)
    b11=tk.Button(root,text="RESTART",height=2,activebackground="lightgrey",width=15,bg='green',font={25,'bold','cursive'},command=restart)
    b11.place(x=700,y=200)    
def load_coins():
    global coins
    names=['O.png','X.png']
    for i in names:
        img=Image.open("images/"+i)
        img=img.resize((215,215))
        img=ImageTk.PhotoImage(img) 
        coins.append(img)
def set_coin(pos):
    global cells
    global turn,win
    global player_pos,comp_pos
    if(win==1):return None
    if(len(player_pos)+len(comp_pos)==9):
        return None
    if(turn==1):
         cells[pos-1].config(image=coins[turn-1])
         cells[pos-1].configure(state='disabled')
         player_pos.append(pos)
         is_winner(player_pos)
         turn=2
         if(win!=1 and (len(player_pos)+len(comp_pos)<9)):
            sys_turn()
    else:
         cells[pos-1].config(image=coins[turn-1])
         cells[pos-1].configure(state='disabled')
         comp_pos.append(pos)
         is_winner(comp_pos)
         turn=1  

def sys_turn():
    while True:
        r=random.randint(1,9)
        if r not in comp_pos and r not in player_pos:
            set_coin(r)
            break
def is_winner(user_pos):
    global f,win
    win_pos=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    f=None 
    for i in win_pos:
        f=0
        for k in i:
            if k in user_pos:
                f=f+1
        if(f==3 and turn==1):
            msg="Player is Winner"
            win=1
            Label=tk.Label(root, text=msg,bg="green",height=5,width=20,font={25,'cursive','bold'})
            Label.place(x=200,y=200)
            break
        elif(f==3 and turn==2):
            msg="Computer is Winner"
            win=1
            Label=tk.Label(root, text=msg,height=5,bg="green",width=20,font={25,'cursive','bold'})
            Label.place(x=200,y=200)
            break
    if(f<3 and (len(player_pos)+len(comp_pos)==9)):
        msg="Game Tie..Play Again"
        Label=tk.Label(root, text=msg,height=5,bg="green",width=20,font={25,'cursive','bold'})
        Label.place(x=200,y=200)
def restart():
    global cells,coins,win,turn,player_pos,comp_pos
    cells.clear()
    coins.clear()
    win=0
    turn=1
    player_pos.clear()
    comp_pos.clear()
    load_coins()
    set_board()

cells=[]
coins=[]
win=0
set_board()
load_coins()
turn=1
player_pos=[]
comp_pos=[]
root.mainloop()