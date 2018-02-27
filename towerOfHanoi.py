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

for disk in range(1, int(disks)+1):
    towers[0].append(disk)

towermoves = [towers[0], [], []]
print(towermoves[0:])

while towermoves[2] != towers[0]:
    if towermoves[2][0:1] < towermoves[0][0:1]:
        print(1)

    time.sleep(1)


