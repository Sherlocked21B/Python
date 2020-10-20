count=0
capital=""
mydict={}
f = open("/home/bijaya/Downloads/countrycapitals.csv","r")
a=f.readlines()
b=input("Enter the name of the country::")
c=b.lower().title()
for i in a:
    count=count+1
for i in range(count):
    con=a[i].split(",")
    mydict[con[0]]=con[1]
print(mydict[c])