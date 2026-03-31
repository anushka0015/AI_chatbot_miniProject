from tkinter import *
root =Tk()
root.geometry("500x500")
root.title("Tic Tac Toe")
frame1 = Frame(root)
frame1.pack()
titleLabel= Label(frame1,text="TIC TAC TOE",font=("Arial",30),bg="pink")
titleLabel.pack()
frame2 =Frame(root)
frame2.pack()

turn="X"

def play(event):
    global turn
    button =event.widget
    if turn=="X":
        button["text"]="X"
        turn ="O"
    else:
        button["text"]="O"
        turn="X"

#row->1

button1=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="skyblue",relief=RAISED,borderwidth=6)
button1.grid(row=0,column=0)
button1.bind("<Button-1>",play)

button1=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="skyblue",relief=RAISED,borderwidth=6)
button1.grid(row=0,column=1)
button1.bind("<Button-1>",play)

button1=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="skyblue",relief=RAISED,borderwidth=6)
button1.grid(row=0,column=2)
button1.bind("<Button-1>",play)

#row->2

button1=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="skyblue",relief=RAISED,borderwidth=6)
button1.grid(row=1,column=0)
button1.bind("<Button-1>",play)

button1=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="skyblue",relief=RAISED,borderwidth=6)
button1.grid(row=1,column=1)
button1.bind("<Button-1>",play)

button1=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="skyblue",relief=RAISED,borderwidth=6)
button1.grid(row=1,column=2)
button1.bind("<Button-1>",play)

#row ->3

button1=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="skyblue",relief=RAISED,borderwidth=6)
button1.grid(row=3,column=0)
button1.bind("<Button-1>",play)

button1=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="skyblue",relief=RAISED,borderwidth=6)
button1.grid(row=3,column=1)
button1.bind("<Button-1>",play)

button1=Button(frame2,text=" ",width=4,height=2,font=("Arial",30),bg="skyblue",relief=RAISED,borderwidth=6)
button1.grid(row=3,column=2)
button1.bind("<Button-1>",play)

root.mainloop()