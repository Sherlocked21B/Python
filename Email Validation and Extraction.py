import re

a = r"123455manojpradhan628@gmail.com is my email and my email is mohanpradhan628@gmail.com"

b = a.split(" ")

c = []

for i in range(len(b)):
    d = re.findall("^[^0-9._]+[a-z0-9]*@[a-z]+.[a-z]+$",b[i])
    c.extend(d)

print(c)