import random

ashish = ["rock", "paper", "scissor"]
x = random.choice(ashish)

shiddhartha = ["rock", "paper", "scissor"]
y = random.choice(shiddhartha)

if x == y:
    print("tie")
elif (x == "rock" and y == "scissor") or (x == "paper" and y == "rock") or (x == "scissor" and y == "paper"):
    print("Ashish Wins")
else:
    print("shiddhartha wins")

print(f"Ashish chose: {x} and shiddhartha chose: {y}")
