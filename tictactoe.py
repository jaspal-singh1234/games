from tkinter import *
root=Tk()
root.minsize(500,400)
root.resizable(0,0)
x=1
def show(e):
    global x
    x=x+1
    if(x%2==0):
        if (e["text"]==""):
            e["text"]="0"
    else:
        if e["text"]=="":
            e["text"]="X"


            
    if(b1["text"]==0 and b2["text"]==0 and b3["text"]==0)
b1=Button(root,text="",font=("Arial",16),width=15,height=5,command=lambda:show(b1))
b1.grid(row=0,column=0,sticky=W)
b2=Button(root,text="",font=("Arial",16),width=15,height=5,command=lambda:show(b2))
b2.grid(row=0,column=1,sticky=W)
b3=Button(root,text="",font=("Arial",16),width=15,height=5,command=lambda:show(b3))
b3.grid(row=0,column=2,sticky=W)
b4=Button(root,text="",font=("Arial",16),width=15,height=5,command=lambda:show(b4))
b4.grid(row=1,column=0,sticky=W)
b5=Button(root,text="",font=("Arial",16),width=15,height=5,command=lambda:show(b5))

b5.grid(row=1,column=1,sticky=W)
b6=Button(root,text="",font=("Arial",16),width=15,height=5,command=lambda:show(b6))
b6.grid(row=1,column=2,sticky=W)
b7=Button(root,text="",font=("Arial",16),width=15,height=5,command=lambda:show(b7))
b7.grid(row=2,column=0,sticky=W)
b8=Button(root,text="",font=("Arial",16),width=15,height=5,command=lambda:show(b8))
b8.grid(row=2,column=1,sticky=W)
b9=Button(root,text="",font=("Arial",16),width=15,height=5,command=lambda:show(b9))
b9.grid(row=2,column=2,sticky=W)
root.mainloop()
