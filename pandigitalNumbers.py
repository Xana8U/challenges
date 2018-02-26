# Checks if all digits from 0 to 9 appear at least once in the number(pandigital
number = input("Give a number")

def occurence(number):
    numdict = dict()
    for i in number:
        if i in numdict:
            numdict[i] = numdict[i] + 1
        else:
            numdict[i] = 1

    print(numdict)


if "0" and "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9" in number:
    print("Number is pandigital")
    occurence(number)
else:
    print("Number is not pandigital")

