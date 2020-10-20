str2=list(input("Enter the list :"))
str2=str2+[' ']
#print(str2)
str1=''
for i in str2:
    str1=str1+i
    if i==' ':
        str1=str1[::-1]
        print(str1,end="")
        str1='' 