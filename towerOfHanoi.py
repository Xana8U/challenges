# Tower of hanoi is a puzzle where you have three disks smallest on top, biggest on bottom and three poles
# at beginning all disks are on the left side pole. Objective is to move all disks into the right side pole
# so that they are in sized order.
# Create an algorithm that does the moves automatically depending on the amount of disks
# standard 3 disk takes 7 moves
# M1 : 1 right , M2 : 2 middle, M3 : 3 middle, M4 : 1 left, M5 : 3 right, M6 : 2 right, M7 : 1 right
#
#       |       |        |
#       1       >        1
#       2       >        2
#       3       >        3
#    ------- -------- -------
import time

disks = input("How many disks does the tower have?")
towers = [[], [], []]
towermoves = [[], [], []]
lastmove = []

def createlist():
    for disk in range(1, int(disks)+1):
        towers[0].append(disk)
        towermoves[0].append(disk)

def isdone():
    if towers[0] == towermoves[2]:
        print("Done!", towermoves)
        input("Program will exit on input:")
        exit()


def solve():
    while True:
        print(towers[0], "this")
        """if not towermoves[2]:
            if towermoves[2][0:1] < towermoves[0][0:1]:
                towermoves[2].insert(0, towermoves[0][0:1][0])
                del towermoves[0][0:1]
                lastmove.append("02")
                if len(lastmove) >= 2:
                    del lastmove[0]
                print(towermoves, "1")
    
        if not towermoves[1] and "01" not in lastmove:
            if towermoves[1][0:1] < towermoves[0][0:1]:
                towermoves[1].insert(0, towermoves[0][0:1][0])
                del towermoves[0][0:1]
                lastmove.append("01")
                if len(lastmove) >= 2:
                    del lastmove[0]
                print(towermoves, "2")
    
        if not towermoves[0] and "20" not in lastmove:
            if towermoves[0][0:1] < towermoves[2][0:1]:
                towermoves[0].insert(0, towermoves[2][0:1][0])
                del towermoves[2][0:1]
                lastmove.append("20")
                if len(lastmove) >= 2:
                    del lastmove[0]
                print(towermoves, "3")
    """
        if towermoves[2][0:1] < towermoves[0][0:1] and "02" not in lastmove:
            towermoves[2].insert(len(towermoves[2]), towermoves[0][0:1][0])
            del towermoves[0][0:1]
            lastmove.append("02")
            if len(lastmove) >= 2:
                del lastmove[0]
            print(towermoves, "4")
            isdone()

        if towermoves[1][0:1] < towermoves[0][0:1] and "01" not in lastmove:
            towermoves[1].insert(len(towermoves[1]), towermoves[0][0:1][0])
            del towermoves[0][0:1]
            lastmove.append("01")
            if len(lastmove) >= 2:
                del lastmove[0]
            print(towermoves, "5")
            isdone()

        if towermoves[0][0:1] < towermoves[1][0:1] and "10" not in lastmove:
            towermoves[0].insert(len(towermoves[0]), towermoves[1][0:1][0])
            del towermoves[1][0:1]
            lastmove.append("10")
            if len(lastmove) >= 2:
                del lastmove[0]
            print(towermoves, "6")
            isdone()

        if towermoves[0][0:1] < towermoves[2][0:1] and "20" not in lastmove:
            towermoves[0].insert(len(towermoves[0]), towermoves[2][0:1][0])
            del towermoves[2][0:1]
            lastmove.append("20")
            if len(lastmove) >= 2:
                del lastmove[0]
            print(towermoves, "7")
            isdone()

        if towermoves[1][0:1] < towermoves[2][0:1] and "21" not in lastmove:
            towermoves[1].insert(len(towermoves[1]), towermoves[2][0:1][0])
            del towermoves[2][0:1]
            lastmove.append("21")
            if len(lastmove) >= 2:
                del lastmove[0]
            print(towermoves, "8")
            isdone()

        if towermoves[2][0:1] < towermoves[1][0:1] and "12" not in lastmove:
            towermoves[2].insert(len(towermoves[2]), towermoves[1][0:1][0])
            del towermoves[1][0:1]
            lastmove.append("12")
            if len(lastmove) >= 2:
                del lastmove[0]
            print(towermoves, "9")
            isdone()
        time.sleep(1)

createlist()
solve()
