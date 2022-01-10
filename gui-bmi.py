#calculate body mass index BMI = kg/m2

from tkinter import*

root = Tk()
root.title('Body Mass Index')
#root.geometry('400x390')
root.maxsize(410,190)
root.minsize(410,190)
root.config(bg = 'black')

def bmi():
    m = int(ent.get())
    kg = int(ent2.get())
    bmi = kg/m*m
    lb = Label(root,text = f 'BMI is {bmi}',bg = 'red')
    lb.place(x = 70,y = 200)
    ent.delete(0,END)
    ent2.delete(0,END)
    
lbl = Label(root,text = 'Body Mass Index',font = ("Arial", 20),fg = "white",bg = "black")
lbl.pack()

lbl2 = Label(root,text = 'Enter your mass:',font = ('Arial',12,"bold"),fg = "white",bg = "black")
lbl2.place(x = 5,y = 40)

ent = Entry(root,bd = 5)
ent.place(x = 230,y = 40)

lbl3 = Label(root,text = 'Enter your height (in meters):',font = ('Arial',12,"bold"),fg = "white",bg = "black")
lbl3.place(x = 5,y = 70)

ent2 = Entry(root,bd = 5)
ent2.place(x = 230,y = 70)

btn = Button(root,text = 'click me!!',font = ('Arial',12,"bold"),fg = "white",bg = "black",command = bmi)
btn.place(x = 170,y = 140)

btn2 = Button(root,text = 'close me!!',font = ('Arial',12,"bold"),fg = "white",bg = "black",command = root.destroy)
btn2.place(x = 70,y = 140)

root.mainloop()
