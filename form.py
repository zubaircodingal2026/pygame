#import necessarie libaries
from tkinter import *
from datetime import date

#create window
root = Tk()
root.title('Getting start with Widgets')
root.geometry('400x300')

#add widgets
#add label
lbl = Label(text="hey there!",fg="white",bg="#072F5F",height=1,width=300)

#add label for getting name as input from user
#using enter widget  to crate a text  box for user to enter detail
name_lbl = Label(text="full name",bg="#3895D3")
Name_entry = Entry()

#function to display a massage
def display() :
    #read input give by user
    name = Name_entry.get()
    #Declaring a global variable
    #to make it accessible anymore in the program
    global Message
    message = "welcome to application! \ntodays date is :"
    greet = "hello"+name+"\n"
    #display detail in a text box
    #specific where to add the detail inside the text box
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
    
#add a text widget to display information/massage
text_box = Text(height=3)