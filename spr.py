import random
player={
    'scissor':2,
    'paper':1,
    'rock':3,
     2:'scissor',
     1:'paper',
     #3:'rock'
     0:'rock'
}
while(1):
    user=input("Enter scissor paper rock : ")
    cpu=random.randint(1,3)
    cpu=cpu % 3
    print("cpu choses")
    print(player[cpu])
    if cpu==0 and player[user]==2:
        print("you lost the game")
    elif cpu==0 and player[user]==3:
        print("Draw")
    else:
        if cpu==player[user]:
            print("The game is draw:")
        elif cpu>player[user]:
            print("you lost the game")
        elif cpu<player[user]:
            print("you won the game")