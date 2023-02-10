import tkinter # imports main library
import random # For random functions
window = tkinter.Tk() #so that there's less confusing brackets
Name = ("Jack","Bob","Ben","Jill","Kate","Annabelle","Sam","Edward","Nelson","Elizabeth","George","Hillary")
def RandomNumber():
     MyRandom = random.choice(Name)
     dice_thrown.configure(text="Random Name: " + str(MyRandom))
MyTitle = tkinter.Label(window, text="Random Name Generator",font="Helvetica 16 bold")
MyTitle.pack()
MyButton = tkinter.Button(window, text="OK", command=RandomNumber) 
MyButton.pack()
dice_thrown = tkinter.Label(window, font="Helvetica 16 bold")
dice_thrown.pack()
window.mainloop()
#TU11
