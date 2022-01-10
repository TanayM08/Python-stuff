from tkinter import *
root=Tk()
root.title('Simple Calculator')
#root.geometry('400x475')
root.minsize(400, 475)
root.minsize(400, 475)

#pic = PhotoImage(file="D:\\linux\\Documents\\Python\\calc.png")#windows
pic = PhotoImage(file='//home//tanay//Documents//Python//calc.png')#linux
root.iconphoto(False,pic)

ent = Entry(root, width=60,borderwidth=10)
ent.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

def ba(a):
    x = ent.get()
    ent.delete(0,END)
    ent.insert(0,str(x)+str(a))

def cr():
    ent.delete(0,END)

def add():
    global F_number
    global maths
    maths = '+'
    x = ent.get()
    F_number = int(x)
    ent.delete(0,END)

def sub():
    global F_number
    global maths
    maths = '-'
    x = ent.get()
    F_number = int(x)
    ent.delete(0,END)

def mul():
    global F_number
    global maths
    maths = '*'
    x = ent.get()
    F_number = int(x)
    ent.delete(0,END)

def div():
    global F_number
    global maths
    maths = '/'
    x = ent.get()
    F_number = int(x)
    ent.delete(0,END)

def eq():
    S_number = int(ent.get())
    ent.delete(0,END)
    if maths == "+":
        ans = F_number+S_number
    elif maths == '-':
        ans = F_number-S_number
    elif maths == '*':
        ans = F_number*S_number
    elif maths == '/':
        ans = F_number/S_number
    ent.insert(0,ans)

btn = Button(root,text='7',padx=40,pady=40,command=lambda:ba(7))
btn.grid(row=1,column=0)

btn2 = Button(root,text='8',padx=40,pady=40,command=lambda:ba(8))
btn2.grid(row=1,column=1)

btn3 = Button(root,text='9',padx=40,pady=40,command=lambda:ba(9))
btn3.grid(row=1,column=2)

btn4 = Button(root,text='4',padx=40,pady=40,command=lambda:ba(4))
btn4.grid(row=2,column=0)

btn5 = Button(root,text='5',padx=40,pady=40,command=lambda:ba(5))
btn5.grid(row=2,column=1)

btn6 = Button(root,text='6',padx=40,pady=40,command=lambda:ba(6))
btn6.grid(row=2,column=2)

btn7 = Button(root,text='1',padx=40,pady=40,command=lambda:ba(1))
btn7.grid(row=3,column=0)

btn8 = Button(root,text='2',padx=40,pady=40,command=lambda:ba(2))
btn8.grid(row=3,column=1)

btn9 = Button(root,text='3',padx=40,pady=40,command=lambda:ba(3))
btn9.grid(row=3,column=2)

btn16 = Button(root,text='0',padx=40,pady=40,command=lambda:ba(0))
btn16.grid(row=4,column=0)

btn10 = Button(root,text='+',padx=40,pady=40,command=add)
btn10.grid(row=1,column=3)

btn11 = Button(root,text='-',padx=40,pady=40,command=sub)
btn11.grid(row=2,column=3)

btn12 = Button(root,text='*',padx=40,pady=40,command=mul)
btn12.grid(row=3,column=3)

btn13 = Button(root,text='/',padx=40,pady=40,command=div)
btn13.grid(row=4,column=3)

btn14 = Button(root,text='=',padx=40,pady=40,command=eq)
btn14.grid(row=4,column=1)

btn15 = Button(root,text='C',padx=40,pady=40,command=cr)
btn15.grid(row=4,column=2)

root.mainloop()
