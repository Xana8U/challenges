# Checks if numer is automorphic, square of the number ends in the number

n = input("Give a range of numbers to check.\n"
          "First the lowest number:")
a = input("Now the highest number:")

rangebank = list()

for i in range(int(n), int(a)):
    rangebank.append(i)

def checkautomorph(rangebank):
    for item in rangebank:
        item = str(item)
        item2 = str(int(item) ** 2)
        if item2[-len(item):] == item:
            print("Number is automorphic {} It's square is:".format(item), item2)
        else:
            continue

print(rangebank)
checkautomorph(rangebank)