from tkinter import *


def signup():

    def cancel():
        exit()

    def submit():
        u=open("/home/bijaya/Desktop/username.txt","a")
        p=open("/home/bijaya/Desktop/password.txt","a")
        uname= entry12.get()
        pword= entry22.get()
        uname=uname
        pword=pword
        print(uname)
        print(pword)
        u.write(uname)
        p.write(pword)
        u.close()
        p.close()

    child = Tk()

    child.geometry("500x300")
    child.title("this is for signup ")

    username1=Label(child,text='User_name')
    password1=Label(child,text='Password')
   
    entry12=Entry(child,width=10)
    entry22=Entry(child,show='*',width=10)
    username1.grid(row=0,column=3)
    password1.grid(row=1,column=3)
    entry12.grid(row=0,column=4)
    entry22.grid(row=1,column=4)

   

    button111= Button(child,text='submit', command = submit)
    button112 = Button(child,text='exit', command=child.destroy)
    button111.grid(row=4,column=3)
    button112.grid(row=4,column=4)
    # printbutton = Button(child,text="print", command=printit)
    # printbutton.grid(row=5,column=0)
     
def login():
    u=open("/home/bijaya/Desktop/username.txt","r")
    p=open("/home/bijaya/Desktop/password.txt","r")
    
    temp1=entry1.get()
    temp2=entry2.get()
    child2=Tk()
    check_uname=str(u.read())
    check_pword=str(p.read())
    temp_uname = check_uname.split()
    temp_pword = check_pword.split()
    
    print(check_uname)
    print(check_pword)

    if temp1 in check_uname :
        if temp2 in check_pword:
            if temp_uname.index(temp1)==temp_pword.index(temp2):
                final_label1=Label(child2,text="you are the authorized user and welcome guyzss",bg='blue',fg='red')
                final_label1.pack(fill=X)
            else:
                final_label2=Label(child2,text="invalid username or password",bg='blue',fg='red')
                final_label2.pack(fill=X)
        else:
            final_label3=Label(child2,text="invalid username or password",bg='blue',fg='red')
            final_label3.pack(fill=X)

    else:
        final_label3=Label(child2,text="This username doesnot exist go and signup first",bg='blue',fg='red')
        final_label3.pack(fill=X)  
    u.close()
    p.close()        

root = Tk()

root.geometry("500x500")
root.title("This is pubg guyzs")

the_label= Label (root,text='pubg_interface',bg='red',fg='orange')
the_label.grid(row=0,column=4,sticky=W)

text1=Label(root,text='User_name')
text2=Label(root,text='Password')

entry1=Entry(root,width=20)
entry2=Entry(root,show='*',width=20)

text1.grid(row=5,column=3)
text2.grid(row=6,column=3)
entry1.grid(row=5,column=4)
entry2.grid(row=6,column=4)

check=Checkbutton(root,text='always remember the password')
check.grid(row=7,column=3)

button1= Button(root,text='login',command=login)
button2= Button(root,text='signup',command=signup)
button1.grid(row=8,column=3)
button2.grid(row=8,column=4)

root.mainloop()