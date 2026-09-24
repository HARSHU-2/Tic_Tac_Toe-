import random

score = 0

while True:
    player = int(input("Choose a number (1-6): "))
    computer = random.randint(1, 6)

    print("Computer:", computer)

    if player == computer:
        print("OUT!")
        break
    else:
        score += player
        print("Score:", score)

print("Final Score:", score)
