class ABBA:
    def __init__(self,initial,final):
        self.initial=initial
        self.final=final
    def canobtain(self):
        if len(self.initial)>=len(self.final):
            print("it is not possible")
        else:
            for i in range(len(self.initial)-1,len(self.final)-1):
                if self.initial[0]==self.final[0]:
                    if self.final[i+1]=="A":
                        self.initial=self.initial+self.final[i+1]
                    else:
                        self.initial=self.initial[::-1]
                        self.initial=self.initial+self.final[i+1]
                else:
                    if self.final[i]=="A":
                        self.initial=self.initial+self.final[i]
                    else:
                        self.initial=self.initial[::-1]
                        self.initial=self.initial+self.final[i]

            if self.initial==self.final:
                print("It is possible")
            else:
                print("It is not possible")
m,n=input("Enter initial and final strings respectively: ").split(" ")
# b= ABBA("B","AABAABABBAB")
b=ABBA(m,n)
b.canobtain()