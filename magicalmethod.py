class distance:
    def __init__(self,meter,centimeter):
        self.x= meter
        self.y= centimeter
    def __add__(self,other):
        a=self.x + other.x
        b=self.y + other.y
        if b>100:
            q=b//100
            re=b%100
            a=a+q
            b=re
        return distance(a,b)

print("for object a:")

(m1,cm1)=int(input("Enter the distance in meter"))
# cm2=int(input("Enter the distance in centimeter"))

print("for object b:")
(m2,cm2)=int(input("Enter the distance in meter"))
# cm2=int(input("Enter the distance in centimeter"))

a= distance(m1,cm1)
b= distance(m2,cm2)

c=a+b

print(c.x)
print(c.y)