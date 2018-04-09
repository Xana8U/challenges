from PIL import Image
import numpy as np
from random import randint

w, h = 512, 512  # Canvas size
data = np.zeros((h, w, 3), dtype=np.uint8)  # Create zero filled array with canvas size parameters and 3 for RGB

bank1 = 0
bank2 = 0
bank3 = 0


def randomizer():
    global bank1, bank2, bank3
    colorform = []

    if bank1 == 0:
        a = randint(0, 255)
    elif bank1 > 235:
        a = randint(bank1 - 20, bank1)
    elif bank1 < 20:
        a = randint(bank1, bank1 + 20)
    else:
        a = randint(bank1 - 20, bank1 + 20)

    if bank2 == 0:
        b = randint(0, 255)
    elif bank2 > 235:
        b = randint(bank2 - 20, bank2)
    elif bank2 < 20:
        b = randint(bank2, bank2 + 20)
    else:
        b = randint(bank2 - 20, bank2 + 20)

    if bank3 == 0:
        c = randint(0, 255)
    elif bank3 > 235:
        c = randint(bank3 - 20, bank3)
    elif bank3 < 20:
        c = randint(bank3, bank3 + 20)
    else:
        c = randint(bank3 - 20, bank3 + 20)

    colorform.append(a)
    colorform.append(b)
    colorform.append(c)
    bank1 = a
    bank2 = b
    bank3 = c
    return colorform


for vertical in range(512):
    data[vertical, 0] = randomizer()
    for horizontal in range(512):
        data[vertical, horizontal] = randomizer()


print(data)
img = Image.fromarray(data, 'RGB')
img.show()
