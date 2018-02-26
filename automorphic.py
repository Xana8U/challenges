# Checks if numer is automorphic, square of the number ends in the number

number = input("Give a number")

a = str(int(number) ** 2)
if a[-len(number):] == number:
    print("It's automorphic")
    print(a)
