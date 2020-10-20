import random
import numpy as np
import math
import matplotlib.pyplot as plt 
shortest_path=np.array([])
matrix1=np.array([])
matrix2=np.array([])
for j in range(0,5):
    (a,b)=(0,0)
    for i in range(0,1000):
        c= random.randint(0,1)
        d= random.randint(0,1)
        if c==0 and d==0:
            b=b-1
        elif c==1 and d==0:
            a=a-1
        elif c==0 and d==1:
            a=a+1
        elif c==1 and d==1:
            b=b+1
        matrix1=np.append(matrix1,a)
        matrix2=np.append(matrix2,b)
    plt.plot(matrix1,matrix2)
    plt.xlabel('x')
    plt.ylabel('y')
    d= (a*a+b*b)**(0.5)
    print(d)
    #for k in range(0,1000):
        #plt.text(matrix1[k],matrix2[k],str(k))
    plt.show()
    shortest_path=np.append(shortest_path,d)
    matrix1=0
    matrix2=0
shortest_path.sort()
print("The shortest path is ")
print(shortest_path[0])

