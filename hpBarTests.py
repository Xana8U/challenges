max_hp = 100
current_hp = 90

smallPotion = 20
LargePotion = 50

defense = 30
wound = 80
damage = wound - defense

hpbooster = 20

def healthbar(max_hp, current_hp, *args):
    base = "[||||||||||]"
    print(args)
    current_hp -= args[0]
    current_hp += args[1]
    max_hp += args[2]
    calc = int(((max_hp - current_hp) / 10))
    if calc != 0:
        print(base[0:-calc], end="")
        print(" "*(len(base)-len(base[0:-calc])), end="")
        print("]")
    else:
        print(base)
    print(current_hp, "/", max_hp)


def healthchange(damage, potion, buff):
    return healthbar(max_hp, current_hp, damage, potion, buff)


healthchange(damage, smallPotion, hpbooster)


