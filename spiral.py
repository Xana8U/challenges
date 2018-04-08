# Once upon a time a small little snek climbed up a tree
import time


floors = 20
treesize = floors * 20
loopcount = 1
ret = 0
tree = []

# for snek
snekhed = "O"
snekbodi = "#"

# loop break
climbed = False

# empty = " " # len 12
for i in range(treesize):
    if loopcount == 1 or loopcount == 15:
        tree.append("|")
    if loopcount == 16:
        tree.append("\n")
        loopcount = 0
    else:
        tree.append(" ")
    loopcount += 1

def drawTree():
    global tree
    for a in tree:
        draw = print(a, end="")
    return str(draw)


spaceit = 4
loop2 = 0 # rowchange pause
while climbed is not True:
    replaced = treesize - spaceit - -36  # spacing on floors is 20 for 45 degrees
    tree[replaced] = snekhed
    print(drawTree())
    time.sleep(0.2)
    if replaced < 20:
        print("You reached the top!")
        climbed = True
    print("\n" * 9)
    tree[replaced] = snekbodi
    spaceit += 14
    loop2 += 1

