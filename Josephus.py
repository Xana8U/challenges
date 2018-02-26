n = int(input("Number of people?"))

for i in range(1, n, 2):
    print("Person {} kills person {} with a sword,".format(i, i+1))
    print("Person {} hands the sword to person {} \n".format(i, i+2))
