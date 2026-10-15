#import necessary packeges
from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfile

#set up root window
window = Tk()
window.title("Codingal text editor")
window.geometry("600x500")
window.rowconfigure(0,minisize=800 ,weight=1)


#Function to open a file
def open_file():
    """Open a file for editor"""
    filepath = askopenfilename(filetypes=[("textfiles","*.txt"), ("All Files","*.*")])
    

    if not filepath :
        return
    txt_edit.delete(1.0,END)
    
    #if a file is open then display the contents of thos file
    with open(filepath,"r") as inputfile :
        #read the content of the input file
        text = input_file.read()
        #insert contents of the file in the editor box
        txt_edit.insert(END ,text)
        input_file.close()
    window.title(f"COdingals file text editor - {filepath}")
    
#function of a save file
def save_file():