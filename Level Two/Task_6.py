import random

start = int(input("Enter your start number: "))
stop = int(input("Enter your stop number: "))
compute_number = random.randint(start, stop)
guess = 0
atemp = 0

while guess != compute_number:
    guess = int(input("Enter the gussing number: "))
    atemp += 1
    if guess > compute_number:
        print("Too high!!, try again")
    elif guess < compute_number:
        print("Too low , try again")
    else:
        print("correct you gussing")



