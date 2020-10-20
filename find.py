import random
str1="dictionary"
b=list(str1)
f=len(b)
str2=f*'@'
a=list(str2)
ik=f//3
print(ik)
for i in range(0,ik):
    r=random.randint(0,(f-1))
    a[r]=b[r]
print(b)
print(a)
