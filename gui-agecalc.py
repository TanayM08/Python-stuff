from tkinter import *
from datetime import date
root=Tk()
root.geometry("400x300")
root.config(bg="black")
root.resizable(width=False,height=False)
root.title('Age Calculator!')
today = date.today()

def exit():
    window.destroy()

def get_age():
    d= int(e1.get())
    m=int(e2.get())
    y=int(e3.get())
    age = today.year-y-((today.month, today.day)<(m,d))
    ti1.config(state='normal')
    ti1.delete('1.0', END)
    ti1.insert(END,age)
    ti1.config(state='disabled')



lb1 = Label(root,text="The Age Calculator!",font=("Arial", 20),fg="white",bg="black").pack()
lb2 = Label(root,font=("Arial",12),text="Enter your birthday which includes: day, month and year.",fg="white",bg="black").pack()

lb_d=Label(root,text="Date: ",font=('Arial',12,"bold"),fg="white",bg="black")
lb_m=Label(root,text="Month: ",font=('Arial',12,"bold"),fg="white",bg="black")
lb_y=Label(root,text="Year: ",font=('Arial',12,"bold"),fg="white",bg="black")
e1=Entry(root,width=5)
e2=Entry(root,width=5)
e3=Entry(root,width=5)
 
bt1=Button(root,text="Calculate Age!",font=("Arial",13),command=get_age)
 
lb3 = Label(root,text="The Calculated Age is: ",font=('Arial',12,"bold"),fg="white",bg="black")
ti1=Text(root,width=5,height=0,state="disabled")
 
bt2=Button(root,text="Exit Application!",font=("Arial",13),command=exit)

lb_d.place(x=100,y=70)
lb_m.place(x=100,y=95)
lb_y.place(x=100,y=120)
lb3.place(x=50,y=200)
e1.place(x=180,y=70)
e2.place(x=180,y=95)
e3.place(x=180,y=120)
bt1.place(x=100,y=150)
bt2.place(x=100,y=230)
ti1.place(x=240,y=203)

root.mainloop()
