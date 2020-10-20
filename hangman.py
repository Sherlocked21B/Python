import re
from os import system
a=['s','@','@','@','@','@','e','@','@']
b=['s','i','m','p','l','i','e','r','y']
c=5
f=len(a)
q=f
x=1
p=[' ']
y=len(p)
while c!=0 and x!=0:
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
        c=c-1
        print("your chances have been deducted")
        print(f"Chances left {c}")

    f=len(a)
    p.append(d)
    y=len(p)
    gi=''.join(a)
    h=re.findall(r"@",gi)
    if h==[]:
        x=0
    if x==0:
        break

if c==0:
    print("you are hanged")
if x==0:
    print(''.join(a))
    print("you won the game")