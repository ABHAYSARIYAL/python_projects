import random

k = random.randint(1,100)
# p = int(input("guess the number between 1  : "))
p = -1
guess = 0
while(p!=k):
    p = int(input("guess the number between 1 to 100: "))

    if(p>k):
        print("lower number please")
        guess +=1
    else:
        print("bigger number please")
        guess +=1


print(f"you guessed the number : {k} correct in {guess} guesses")