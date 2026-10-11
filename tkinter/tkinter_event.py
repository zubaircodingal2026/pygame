#import necessary libaries 
from tkinter import *

#create window
window = Tk()
window.title ("Event Handler")
window.geometry("100x100")

#event handler for keypress
def handle_keypress(event):
    """print the character associated to the key pressed"""
    print(event.char)
    
#bind keypress event to handle _keypress()
window.bind("<Key>", handle_keypress)

#Event handeler for button click
def handle_click(event):
    print("\nThe button was clicked")
    
button = Button(text="click me!")
button.pack()

# BIND LICK EVENT TO HANDLE_CLICK()
button.bind("<Button-1>",handle_click)

#start the GUI event loop
window.mainloop()