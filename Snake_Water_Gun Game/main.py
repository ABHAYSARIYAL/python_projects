'''
1 for snake
-1 for water
0 for gun
'''
import random



computer =random.choice([-1,0,1])
youstr = input("Enter your choice : ")
youDict = {
    "s" : 1,
    "w" : -1,
    "g" : 0
}
reverse_youDict = {
    1 : "snake",
    -1 : "water",
    0 : "gun"
}
you = youDict[youstr]
print(f"computer choose :{reverse_youDict[computer]} \nyou choose : {reverse_youDict[you]}")
if(computer==you):
    print("it's a draw!")
else:
    if(computer==-1 and you==1):
        print("you win")
    elif(computer == -1 and you==0):
        print("you lose!")
    elif(computer==1 and you==0):
        print("you win")
    elif(computer==1 and you==-1):
        print("you lose")
    elif(computer==0 and you==1):
        print("you win")
    elif(computer==0 and you==-1):
        print("you lose")
    else:
        print("something went wrong")
