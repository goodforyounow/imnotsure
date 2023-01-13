import random

random_number = random.randint(0, 10)
print(random_number)
print("Hello. Welcome to the random number generator game.  The number will be between 0 - 10")
user_input = int(input("Pick a number: "))
if random_number != user_input:
    print("no ")
else:
    print("smart ! It's the answer")
    print(random_number)
