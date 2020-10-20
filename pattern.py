n=int(input("Enter the dimension of tree:"))
m=n
j=1
for i in range(0,n):
    print(f"{(m-1)*' '} {(i+j)*'*'}")
    m=m-1
    j=j+1
for i in range(0,n):
    print((n-1)*' ',end="")
    print('*')