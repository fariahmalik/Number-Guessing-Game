import random
from tkinter import *

root = Tk()
root.geometry('630x400')
root.resizable(0,0)
root.title("Guess the number")
root.config(bg='light blue')
# logo=PhotoImage(file='youtube1.png')
# imgLbl = Label(root,image=logo)
# imgLbl.place(x=100,y=5)

attempts=10

text = StringVar()
text.set('You have 10 attempts remaining, Good Luck!! ')
ans = random.randint(1, 99)

def guess_number():
    global attempts
    global text
    attempts -= 1
    guess = int(entry.get())
    if ans == guess:
        text.set('You win the game!!!')
        btn_check.place_forget()
    if attempts == 0:
        text.set('You are out of attempts')
        btn_check.place_forget()
    elif ans > guess:
        text.set('Incorrect- remaining attempts are '+str(attempts)+'\n attempts remaining - Go higher')
    elif ans < guess:
        text.set('Incorrect- remaining attempts are '+str(attempts)+'\n attempts remaining - Go Lower')
        return

def quit():
    root.destroy()

Guess_attempts= Label(root, textvariable=text, font = 'arial 15')
Guess_attempts.place(x=100,y=270)
Label(root, text = 'Enter Your Guess between 1 to 99', font = 'arial 15 bold').place(x= 140 , y = 40)
entry = Entry(root, width = 40)
entry.place(x = 170, y = 100)
btn_check =Button (root, text = 'Check', font = 'arial 15 bold' ,bg = 'white smoke', padx = 2,command=guess_number)
btn_check.place(x=250 ,y = 160)
btn_quit= Button (root, text = 'Quit', font = 'arial 15 bold' ,bg = 'white smoke', padx = 1,command=quit,width=6).place(x=250 ,y = 220)
root.mainloop()