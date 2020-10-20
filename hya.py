import re
from os import system
a=['s','@','@','@','@','@','e']
b=['s','i','m','p','l','i','e']
complete = ['s','i','m','p','l','i','e']
c=5
f=len(a)
q=f
x=1
p=[' ']
y=len(p)
while x!=0:
    if a == complete:
        print("".join(a))
        print("You won!")
        break
    if c==0:
        break
    while a != complete:
        g=''.join(a)
        print(g)
        print(f"Lives {c}")

        d=input("\nEnter the guessing character::")
        
        for l in p:
            if d==l:
                print("already entered")

        for i in b:
            if d==i:
                e=b.index(d)
                a[e]=d
                b[e]='@'

            else:
                f=f-1
        for k in p:
            if d!=k:
                y=y-1
        if f==0 and y==0:
            if c> 0:
                c=c-1
                print("your chances have been deducted")
                print(f"Chances left {c}")
            else:
                print("You are hanged")
                break;

        f=len(a)
        p.append(d)
        y=len(p)
        h=re.findall(r"@",g)
        if h==[]:
            x=0

