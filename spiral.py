import time
import os

object = "( ╰∪╯ )"
empty = " " # len 12

loopcount = 0
ret = 0

def App():
    global loopcount
    global ret
    visual = ""
    if loopcount == 9:
        ret = 1
    elif loopcount == 0:
        ret = 0
    if loopcount < 9 and ret == 0:
        visual = empty * loopcount + object
        loopcount += 1
    elif ret == 1:
        loopcount -= 1
        visual = empty * loopcount + object
    return visual

while True:
    print(App())
    print(App())
    print(App())
    print(App())
    print(App())
    print(App())
    print(App())
    print(App())
    print(App())
    print(App())
    print(App())
    print(App())
    print(App())
    print(App())
    print(App())
    time.sleep(0.5)
    os.system("cls")

# while True:
#     if loopcount < 8:
#         print(null*loopcount + object)
#         loopcount += 1
#         time.sleep(0.5)

