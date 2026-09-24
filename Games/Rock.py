import random

a = random.choice(["rock", "paper", "scissors"])
b = input("Choose rock/paper/scissors: ")

print("Computer:", a)

if a == b:
    print("Draw!")
elif (b == "rock" and a == "scissors") or (b == "paper" and a == "rock") or (b == "scissors" and a == "paper"):
    print("You win!")
else:
    print("You lose!")
