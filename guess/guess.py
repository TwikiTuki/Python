import random


def get_guess():
    guess = input("Enter your Guess: ")
    if (guess == "Exit"):
        exit()
    if (not guess.isdigit()):
        print("The input must be a number. ", end="")
        guess = get_guess()
    guess = int(guess)
    if (guess <= 0 or guess >= 100):
        print("The input must be a number between 1 and 99. ", end="")
        guess = get_guess()
    return (guess)


num = int(random.random() * 98 + 1)
#print("the answer is:", num)

guess = get_guess()
count = 1
while (guess != num):
    if (guess < num):
        print(f"The number {guess} is too low")
    else:
        print(f"The number {guess} is too high")
    count += 1
    guess = get_guess()
if (num == 42):
    print("Wow looks like we have a very nice writer for this game")
if (count == 1):
    print("Congratulations you made it at first attempt")
    exit()
print(f"Congratulations you got it at try {count}")
