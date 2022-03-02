#importing modules
from tkinter import *
from tkinter import messagebox
from random import *
#CUSTOMIZING COLOURS
GREEN = "#007d21"
YELLOW = "#C9B458"
LIGHTGREY ="#787C7E"
GREY = "#3a3a3c"
#choosing a word
data = open("D:\Programming\words.txt", "r")
for line in data:
    wordbank =line.split()
word = choice(wordbank)
word = word.upper()
#creating main window
w = Tk()
w.title("WORDPLAY")
w.config(bg="white")
#instruction menu
def click():
    global popup
    popup = Toplevel(w)
    popup.title("Instructions")
    popup.geometry("400x700")
    popup.config(bg="white")
    pop1 = Label(popup, text="How To Play", bg=YELLOW, fg=GREY,font=("georgia", 20, "bold"))
    pop1.pack(side=TOP, fill=X)
    pop2 = Label(popup, text="\n \nThe rules are very simple: \n \n Guess the WORD in six tries. \n \n Each guess must be a valid 5 letter word. \n Hit the enter button to submit. \n \n After each guess the colour of tiles will \n change to show how close your guess \n was to the word\n \nIf the letter is guessed correctly and is in \n the correct place, it will be highlighted \nin GREEN, \n \nIf the letter is in the word,\n but in the wrong place - in YELLOW, \n \n and if the letter is not in the word,\n it will remain GREY.", font=("georgia", 10), bg="white", fg="black", justify="left")
    pop2.pack(fill=X)
    eg = Frame(popup, bg="white")
    eg.place(x=100, y=420)
    green_eg = Label(eg, width=3, height=3, text="K", bg=GREEN, fg="white", relief="solid", borderwidth=2 ,font=("helvetica",10,"bold"))
    green_eg.grid(row=0, column=0, padx=2, pady=4)
    green_eg = Label(eg, width=3, height=3, text="A", fg="black", bg="white", relief="solid", borderwidth=2,font=("helvetica",10,"bold"))
    green_eg.grid(row=0, column=1, padx=2, pady=4)
    green_eg = Label(eg, width=3, height=3, text="R", fg="black", bg="white", relief="solid", borderwidth=2,font=("helvetica",10,"bold"))
    green_eg.grid(row=0, column=2, padx=2, pady=4)
    green_eg = Label(eg, width=3, height=3, text="M", fg="black", bg="white", relief="solid", borderwidth=2,font=("helvetica",10,"bold"))
    green_eg.grid(row=0, column=3, padx=2, pady=4)
    green_eg = Label(eg, width=3, height=3, text="A", fg="black", bg="white", relief="solid", borderwidth=2,font=("helvetica",10,"bold"))
    green_eg.grid(row=0, column=4, padx=2, pady=4)
    yellow_eg = Label(eg, width=3, height=3, text="C", fg="black", bg="white", relief="solid", borderwidth=2,font=("helvetica",10,"bold"))
    yellow_eg.grid(row=1, column=0, padx=2,pady=4)
    yellow_eg = Label(eg, width=3, height=3, text="L", fg="white", bg=YELLOW, relief="solid", borderwidth=2,font=("helvetica",10,"bold"))
    yellow_eg.grid(row=1, column=1, padx=2,pady=4)
    yellow_eg = Label(eg, width=3, height=3, text="I", fg="black", bg="white", relief="solid", borderwidth=2,font=("helvetica",10,"bold"))
    yellow_eg.grid(row=1, column=2, padx=2,pady=4)
    yellow_eg = Label(eg, width=3, height=3, text="C", fg="black", bg="white", relief="solid", borderwidth=2,font=("helvetica",10,"bold"))
    yellow_eg.grid(row=1, column=3, padx=2,pady=4)
    yellow_eg = Label(eg, width=3, height=3, text="K", fg="black", bg="white", relief="solid", borderwidth=2,font=("helvetica",10,"bold"))
    yellow_eg.grid(row=1, column=4, padx=2,pady=4)
    yellow_eg = Label(eg, width=3, height=3, text="F", fg="black", bg="white", relief="solid", borderwidth=2,font=("helvetica",10,"bold"))
    yellow_eg.grid(row=2, column=0, padx=2,pady=4)
    yellow_eg = Label(eg, width=3, height=3, text="A", fg="black", bg="white", relief="solid", borderwidth=2,font=("helvetica",10,"bold"))
    yellow_eg.grid(row=2, column=1, padx=2,pady=4)
    yellow_eg = Label(eg, width=3, height=3, text="L", fg="white", bg=LIGHTGREY, relief="solid", borderwidth=2,font=("helvetica",10,"bold"))
    yellow_eg.grid(row=2, column=2, padx=2,pady=4)
    yellow_eg = Label(eg, width=3, height=3, text="S", fg="black", bg="white", relief="solid", borderwidth=2,font=("helvetica",10,"bold"))
    yellow_eg.grid(row=2, column=3, padx=2,pady=4)
    yellow_eg = Label(eg, width=3, height=3, text="E", fg="black", bg="white", relief="solid", borderwidth=2,font=("helvetica",10,"bold"))
    yellow_eg.grid(row=2, column=4, padx=2,pady=4)
#menubar
topbar = Frame(w, bg=GREY)
topbar.pack(side=TOP, fill=X)
Instructions= Button(topbar, text="Instructions", command=click, bg=GREY, fg="white",font=("Georgia",12,"bold"))
Instructions.grid(row=0, column=0, )
name_lbl = Label(topbar, text="WordPlay: Guess The Hidden Word",font=("Georgia",18,"bold"),bg=GREY, fg="white") 
name_lbl.grid(row=0, column=1, padx=680)
#entryboxes
f1 = Frame(w, bg="white")
f1.place(x=800, y=100)
turn = 0
rows = [None,None,None,None,None,None]
def createRow(rowIdx):
    global rows
    e0= Entry(f1, width=5, font=("helvetica",18,"bold"), justify=("center"))
    e0.grid(row=rowIdx, column=0, ipady=15 ,padx=5, pady=5)
    e1= Entry(f1, width=5, font=("helvetica",18,"bold"), justify=("center"))
    e1.grid(row=rowIdx, column=1, ipady=15 ,padx=5, pady=5)
    e2= Entry(f1, width=5, font=("helvetica",18,"bold"), justify=("center"))
    e2.grid(row=rowIdx, column=2,ipady=15, padx=5, pady=5)
    e3= Entry(f1, width=5, font=("helvetica",18,"bold"), justify=("center"))
    e3.grid(row=rowIdx, column=3,ipady=15, padx=5, pady=5)
    e4= Entry(f1, width=5, font=("helvetica",18,"bold"), justify=("center"))
    e4.grid(row=rowIdx, column=4,ipady=15, padx=5, pady=5)
    rows[rowIdx] = [e0,e1,e2,e3,e4]
#to create first row
createRow(0)
#disabled entry boxes
for i in range(1,6):
    e0= Entry(f1, width=5, font=("helvetica",18,"bold"), state="disabled" )
    e0.grid(row=i, column=0, ipady=15 ,padx=5)
    e1= Entry(f1, width=5, font=("helvetica",18,"bold"), state="disabled" )
    e1.grid(row=i, column=1, ipady=15 ,padx=5)
    e2= Entry(f1,width=5, font=("helvetica",18,"bold") , state="disabled")
    e2.grid(row=i, column=2,ipady=15, padx=5)
    e3= Entry(f1,width=5, font=("helvetica",18,"bold") , state="disabled")
    e3.grid(row=i, column=3,ipady=15, padx=5)
    e4= Entry(f1, width=5, font=("helvetica",18,"bold"), state="disabled")
    e4.grid(row=i, column=4,ipady=15, padx=5)
#checking the word
def answer():
    global turn
    ans = ""
    a0 = rows[turn][0].get()
    ans += a0.upper()
    a1 =rows[turn][1].get()
    ans += a1.upper()
    a2 =rows[turn][2].get()
    ans += a2.upper()
    a3 =rows[turn][3].get()
    ans += a3.upper()
    a4 =rows[turn][4].get()
    ans += a4.upper()
    #checking if the word only has alphabetical characters
    x = "1234567890@#$%^&*!?. "
    y = 0
    for i in ans:
        if i in x:
            y += 1
    if y>0:
        messagebox.showerror("TYPE ERROR", "Please only enter alphabetical characters to take a guess")
    else:
        if len(ans) == 5:
            #to check if the word is valid
            if ans.upper() not in wordbank:
                messagebox.showerror("TYPE ERROR", "Please enter a valid word")
            else:
                for i in range(len(ans)):
                #when the letter is correctly placed
                    if ans[i] == word[i]:
                        la= Label(f1, width=5, bg=GREEN, fg="white", relief="solid", borderwidth=2, font=("helvetica",18,"bold"),text=(ans[i]).upper())
                        la.grid(row=turn, column=i, ipady=15 ,padx=5, pady=5) 
                #when the letter is in the word but wrongly placed
                    if ans[i] in word and not ans[i]==word[i]:
                        la= Label(f1, width=5, bg=YELLOW, fg="black",relief="solid", borderwidth=2, font=("helvetica",18,"bold"),text=(ans[i]).upper())
                        la.grid(row=turn, column=i, ipady=15 ,padx=5, pady=5)
                #when the letter is not in the word
                    if ans[i] not in word:
                        la= Label(f1, width=5, bg=LIGHTGREY, fg="white", relief="solid", borderwidth=2,font=("helvetica",18,"bold"),text=(ans[i]).upper())
                        la.grid(row=turn, column=i, ipady=15 ,padx=5, pady=5)
                if ans == word:
                    messagebox.showinfo("YOU WIN", "CONGRATULATIONS! YOU GUESSED THE WORD CORRECTLY")
                #for next turn when incorrect 
                else:
                    turn +=1
                    if turn <= 5:
                        createRow(turn)            
                    else:
                        messagebox.showinfo("YOU LOSE", f"YOU LOSE! THE WORD WAS {word.upper()}")  
                #when multiple entries are given in a entrybox                    
        else:
            messagebox.showerror("Type Error", "To make a guess, Please make sure you only enter one character in every entry box")           
button1 = Button(w, text="ENTER", bg=YELLOW, fg=GREY, font=("Georgia", 18,"bold"),command=answer)
button1.place(x=950,y=700)
w.mainloop()


