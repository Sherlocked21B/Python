import re

# str1 = "grey greyeyed grind"
str=r"1245i9hitme8827hardontheface4774@gmail.com it is my gmail@45email abc253@email.com"
# a = re.findall("^g[a-z]*y$",str1)
a=re.findall('\s*[a-z]+[a-z0-9]*@[a-z]+.[a-z]+',str)
# for i in range(len(a)):
#     a[i] = a[i][1::]

print(a)