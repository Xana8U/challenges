import string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase

instring = input("Input string to reciprocate:")

placement = 0
output = ""


for letter in instring:
    if letter in lowercase:
        for i in lowercase:
            placement += 1
            if i == letter:
                output += lowercase[-placement]
        placement = 0

    elif letter in uppercase:
        for i in uppercase:
            placement += 1
            if i == letter:
                output += uppercase[-placement]
        placement = 0

    else:
        output += " "

print(output)
