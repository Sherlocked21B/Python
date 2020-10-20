from tkinter import *
import random

global count

def printit(label1):
    def again():
        r=str(random.randint(1,5))
        label1.config(text=r,bg="yellow")
        count=r
        button.config(text="stop",command=root.destroy)
        label1.after(100,again)
    again()

def stop():
    return 0

root = Tk()

root.title("decide")
root.geometry("1000x500")
root.config(background='yellow')

picture= PhotoImage(file="/home/bijaya/Downloads/Realistic_bunny_2.gif")
label= Label(root,compound=LEFT,bg="yellow",text="press okey to stop the flow",
                font="calibri 50 underline",image=picture)

label.grid(row=1)
label1=Label(root,text='1',font="calibri 300 underline")
label1.grid(row=4)

button = Button(root,text="stop",command=stop)
button.grid(row=6)

printit(label1)

label1=Label(root,text=str(count),font="calibri 300 underline")
label1.grid(row=4)

root.mainloop()