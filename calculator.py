from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    # print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
     
        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


root = Tk()
root.geometry("544x700")
root.maxsize(544,700)
root.title("Calculator")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill = X,padx=10,pady=10,ipadx=8)

# First Row
f = Frame(root,bg="grey",padx=6,pady=6)

b = Button(f,text="9",font="lucida 35 bold")
b.pack(side=LEFT,padx=28,pady=20)
b.bind("<Button-1>",click)

b = Button(f,text="8",font="lucida 35 bold")
b.pack(side=LEFT,padx=28,pady=20)
b.bind("<Button-1>",click)

b = Button(f,text="7",font="lucida 35 bold")
b.pack(side=LEFT,padx=28,pady=20)
b.bind("<Button-1>",click)

b = Button(f,text="+",font="lucida 35 bold")
b.pack(side=LEFT,padx=28,pady=20)
b.bind("<Button-1>",click)

f.pack()

# Second Row
f = Frame(root,bg="grey",padx=12,pady=10)

b = Button(f,text="6",font="lucida 35 bold")
b.pack(side=LEFT,padx=28,pady=20)
b.bind("<Button-1>",click)

b = Button(f,text="5",font="lucida 35 bold")
b.pack(side=LEFT,padx=28,pady=20)
b.bind("<Button-1>",click)

b = Button(f,text="4",font="lucida 35 bold")
b.pack(side=LEFT,padx=28,pady=20)
b.bind("<Button-1>",click)

b = Button(f,text="-",font="lucida 35 bold")
b.pack(side=LEFT,padx=28,pady=20)
b.bind("<Button-1>",click)

f.pack()

# Third Row
f = Frame(root,bg="grey",padx=5,pady=5)

b = Button(f,text="3",font="lucida 35 bold")
b.pack(side=LEFT,padx=28,pady=20)
b.bind("<Button-1>",click)

b = Button(f,text="2",font="lucida 35 bold")
b.pack(side=LEFT,padx=28,pady=20)
b.bind("<Button-1>",click)

b = Button(f,text="1",font="lucida 35 bold")
b.pack(side=LEFT,padx=28,pady=20)
b.bind("<Button-1>",click)

b = Button(f,text="X",font="lucida 35 bold")
b.pack(side=LEFT,padx=28,pady=20)
b.bind("<Button-1>",click)

f.pack()

# Fourth Row
f = Frame(root,bg="grey",padx=10,pady=10)

b = Button(f,text="0",font="lucida 35 bold")
b.pack(side=LEFT,padx=28,pady=20)
b.bind("<Button-1>",click)

b = Button(f,text="C",font="lucida 35 bold")
b.pack(side=LEFT,padx=28,pady=20)
b.bind("<Button-1>",click)

b = Button(f,text="=",font="lucida 35 bold")
b.pack(side=LEFT,padx=28,pady=20)
b.bind("<Button-1>",click)

b = Button(f,text="/",font="lucida 35 bold")
b.pack(side=LEFT,padx=28,pady=20)
b.bind("<Button-1>",click)

f.pack()

root.mainloop()