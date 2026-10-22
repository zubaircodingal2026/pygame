#import necessary libaries
from tkinter import *

#setting up the window
root = Tk()
root.geometry("400x300")
root.title("main")

#function to open the new (top level) window
def topwin():
    #setting up the main window
    top = Toplevel()
    top.geometry("180x100")
    top.title("top title")
    
    #adding a label widget to top window
    l2 =Label(top,text="This is top level window")
    l2.pack() 
    
    top.mainloop() 
    
#adding a label and button widget to root (main) window
l = Label(root , text="this is root window")
btn = Button(root , text="Click here to open another window", command=topwin)

#arrange widgets
l.pack()
btn.pack()

root.mainloop()