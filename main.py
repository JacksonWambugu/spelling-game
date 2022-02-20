import tkinter
import pyttsx3

from tkinter import *
from textblob import TextBlob

root=Tk()

root.title("Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")
root.resizable(False,False)

engine=pyttsx3.init()
button_mode=True
def customize():
    global button_mode
    if button_mode:
        button1.config(image=off,bg="#26242f",activebackground="#26242f")
        root.config(bg="#26242f")
        button_mode=False
    else:
        button1.config(image=on,bg="white",activebackground="#26242f")
        root.config(bg="white")
        button_mode=True

off=PhotoImage(file="light.png")
on=PhotoImage(file="dark.png")


button1=Button(root,image=on,bd=0,bg="white",activebackground="white",command=customize)
button1.place(x=500,y=0)



def check_spelling():
    word=enter_text.get()
    a=TextBlob(word)
    right=str(a.correct())
    
    cs=Label(root,text="Correct spelling  is : ",font=("poppins",20),bg="#dae6f6",fg="#364971")
    cs.place(x=100,y=250)
    spell.config(text=right)
    r_ight=(" ".join(right))
    engine.setProperty('rate',150)
    engine.say("the correct spelling is ")
    engine.setProperty('rate',100)
    engine.say(r_ight)
    engine.setProperty('rate',140)
    
    engine.say(right)
    engine.runAndWait()


heading=Label(root,text="Spelling Checker",font=("Trebuchet MS",30,"bold"),bg="#dae6f6",fg="#364971")
heading.pack(pady=(50,0))

enter_text=Entry(root,justify="center",width=30,font=("poppins",25),bg="white",border=2)
enter_text.pack(pady=10)
enter_text.focus()


button=Button(root,text="Check",font=("arial",20,"bold"),fg="white",bg="cyan",command=check_spelling)
button.pack()

spell=Label(root,font=("poppins",20),bg="#dae6f6",fg="#364971")
spell.place(x=350,y=250)



root.mainloop()