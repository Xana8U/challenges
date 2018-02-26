n = input("Give a range of numbers to check.\n"
          "First the lowest number:")
a = input("Now the highest number:")

rangebank = []

# Add all numbers in given range for checking
for i in range(int(n), int(a)):
    rangebank.append(i)


def armcheck(rangebank):
    adds = 0
    numbank = []
    for item in rangebank:
        item = str(item)
        for inner in item:
            a = int(inner)**3
            numbank.append(a)

        while len(numbank) < len(n):
            number = numbank[0]+numbank[1]
            del numbank[1]

        for i in numbank:
            adds = adds + i

        if int(item) == adds:
            print("{} is an Armstrong number".format(str(item)))
        else:
            pass
        numbank = []
        adds = 0
armcheck(rangebank)
