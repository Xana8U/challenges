# Check if a number is an armstrong number
# every number in n in power of three and added together after equal n
# 153
# 1**3 + 5**3 + 3**3 = 153

n = input("Number?")

numbank = []
adds = 0
for i in n:
    a = int(i)**3
    numbank.append(a)

while len(numbank) < len(n):
    number = numbank[0]+numbank[1]
    del numbank[1]

for i in numbank:
    adds = adds + i

if int(n) == adds:
    print("It is an Armstrong number")
else:
    print("Its not an Armstrong number")