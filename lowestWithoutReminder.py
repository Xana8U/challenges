# test every number between 1-100 if it can be divided by all numbers between 1-10 without there being any reminder

checker = list()
loop = 1
for number in range(1, 10001):
    print(loop)
    for modulo in range(1, 11):
        if number % modulo == 0:
            checker.append(modulo)
            print("added one")

    if len(checker) == 10:
        print("FOUND IT HERE: ", number)
        break
    else:
        checker = list()

    loop += 1

