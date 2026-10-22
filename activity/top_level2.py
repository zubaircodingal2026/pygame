from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

#_____________________________
#setting up main window
#_____________________________
root = Tk()
root.title("Denomination counter")
root.configure(bg="light blue")
root.geometry("650x400")

#_____________________________________
#adding image and label in main window
#_____________________________________
upload = Image.open("images.jpeg")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)

label = Label(root,image=image,bg="light blue")
label.place(x=180,y=20)

label1 = Label(root, text="Hey user! Welcome to domination counter application",bg="light blue")


label1.placw(relx=0.5,y=340,anchor=CENTER)

#____________________________________________
#function to open message box
#____________________________________________
def msg():
    MsgBox = messagebox.showinfo("Alert","Do you want to calculate the dinomination count" )
    
    if MsgBox == "ok":
        topwin()
    
#________________________________
#adding button in the main window
#_______________________________
button1 = Button(root,text="lets get started",command=msg,bg="brown",fg="white")

button1.plzce(x=260,y=360)

#___________________________________
#function for opening new/top window
#___________________________________
def topwin():
    top = Toplevel()
    top.title("Domination calculator")
    top.configure(bg="light gray")
    top.geometry("600x350+50+50")
    
    label = Label(top,text="enter tool amount",bg="light gray")
    entry = Entry(top)
    
    lbl = label(top,text="Here are the numbers of notes for each dinamination",bg="light gray")
    
    l1 = label(top,text="2000",bg="light gray")
    l1 = label(top,text="500",bg="light gray")
    l1 = label(top,text="100",bg="light gray")
    
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    
    
    #_____________________
    #calculation function
    #_____________________
    def calculator():
        try:
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100
            
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            
            t1.insert(END,str(note2000))
            t1.insert(END,str(note500))
            t1.insert(END,str(note100))
        except ValueError:

            messagebox.showerror("Error", "Please enter a valid number.")
    
    
    
    
    
    
    btn = Button(top,text="Calculator",command=calculator,bg="brown"fg="white")
            #_________________________________
            #placing widgets
            #_______________________________
    label.place(x=230, y=50)

    entry.place(x=200, y=80)

    btn.place(x=240, y=120)

    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)

    l2.place(x=180, y=230)

    l3.place(x=180, y=260)

    t1.place(x=270, y=200)

    t2.place(x=270, y=230)

    t3.place(x=270, y=260)
            
    top.mainloop()
            
root.mainloop()