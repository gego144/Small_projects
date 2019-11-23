import random

#setting up variables and users guess
amountflipped = 0
heads = 0
tails = 0
guess = input("Do you think heads or tails will appear more?: ")
#main loop of coin being flipped
while amountflipped < 1000:
    x = random.randint(1, 2)
    if x == 1:
        heads = heads+1
    else:
        tails = tails+1
    print(x)
    amountflipped += 1

#printing out the percent of the greater side of the coin
if heads > tails:
    percent = float(heads / amountflipped) * 100
    print("Heads occurs %.2f" %percent + " % of the time")
else:
    percent = float(tails / amountflipped) * 100
    print("Tails occurs %.2f" %percent + " % of the time")

#printing out how many times each side of the coin appeared
print("Heads appeared " + str(heads) + " times and tails appeared " + str(tails) + " times")

#printing whether or not the user was correct with their guess
if guess == "heads" and heads > tails:
    print("You win!")
elif guess == "heads" and heads < tails:
    print("You lose.")
elif guess == "tails" and tails > heads:
    print("You win!")
else:
    print("You lose.")
