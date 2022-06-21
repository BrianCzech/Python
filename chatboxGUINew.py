from tkinter import *
root=Tk()

def send():
    send="You =>"+e.get()
    txt.insert(END, "\n"+send)
    if(e.get()=="Hello"):
        txt.insert(END, "\n"+"Bot => Hi")
    elif(e.get()=="Hi"):
        txt.insert(END, "\n"+"Bot => Hello") 
    elif(e.get()=="How are you"):
        txt.insert(END, "\n"+"Bot => fine, and you")  
    elif(e.get()=="Fine"):
        txt.insert(END, "\n"+"Bot => nice to hear")  
    elif(e.get()=="Bye"):
        txt.insert(END, "\n"+"Bot => have a nice day")  
    else:
        txt.insert(END, "\n"+"Bot => sorry, I didn't get it") 
    e.delete(0,END)

txt=Text(root)
txt.grid(row=0,column=0,columnspan=2)
e=Entry(root,width=100)

send=Button(root, text='Send', command=send).grid(row=1,column=1)
e.grid(row=1,column=0)


root.title('Chat Box')
root.mainloop()
