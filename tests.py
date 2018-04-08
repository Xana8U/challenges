import random


def random_digit():
    y = random.randint(0, 9)
    return y

this = random_digit()

Answer = False

while not Answer:
    def number_checker(x, y):
        global Answer
        if x == y:
            print("Answer: Correct.\n")
            Answer = True
        if x < y:
            print("Answer: Incorrect. Guess Higher.\n")
        if x > y:
            print("Answer: Incorrect. Guess Lower.\n")

    def guess_digit():
        y = this
        x = int(input("Enter a digit:"))
        return number_checker(x, y)

    guess_digit()