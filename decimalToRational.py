# 0.75 = 3/4 , 0.5 = 1/2, 0.3333 = 1/3 and so on
# this was kind of a pain in my butt :D this took longest so far

floating = input("Give a number to convert:")

startn = len(floating) - 1

floating = float(floating)

highest = 1

for i in range(1, startn):
    highest *= 10

calc1 = int(floating * highest)
calc2 = int(highest)

while True:
    if calc1 % 25 == 0 and calc2 % 25 == 0:
        calc1 /= 25
        calc2 /= 25
    elif calc1 % 5 == 0 and calc2 % 5 == 0:
        calc1 /= 5
        calc2 /= 5
    elif calc1 % 2 == 0 and calc2 % 2 == 0:
        calc1 /= 2
        calc2 /= 2
    else:
        break

print("Fractional = " + str(int(calc1)) + "/" + str(int(calc2)))
