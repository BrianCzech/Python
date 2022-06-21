#Library
from tkinter import *

#Create the tkinter object (this reporesents the parent window)
root=Tk()

#Title
root.title('Chat Bot')

#Dimensions
root.geometry('400x500')



#Create a main menu bar
main_menu=Menu(root)

#Create the sub menu
file_menu=Menu(root)
file_menu.add_command(label='New..')
file_menu.add_command(label='Save As..')
file_menu.add_command(label='Exit')



main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_command(label='Edit')
main_menu.add_command(label='Quit')
root.config(menu=main_menu)

#Create chat window
chatWindow=Text(root, bd=1, bg='yellow', width =50, height=8)
chatWindow.place(x=6,y=6, height=385, width=370)


#Create the message window
messageWindow=Text(root, bg='light green', height=4, width=30, )
messageWindow.place(x=128, y=400, height=88, width=260)


#Create a send button


Button=Button(root, text='Send', bg='blue', activebackground='light blue',width=12, height=5)

Button.place(x=6, y=400, height=88, width=120)

#Add a scroll bar
scrollbar=Scrollbar(root, command=chatWindow.yview())
scrollbar.place(x=375,y=5,height=385)








root.mainloop()