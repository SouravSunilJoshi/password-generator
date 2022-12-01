import random

def tellpass(password):
    shuff = []
    for x in password:
        shuff.append(x)

    random.shuffle(shuff)
    shuff = "".join(shuff)

    print(shuff)


tellpass("passissourav")