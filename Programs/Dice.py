import random

def dice():
    total = 0
    for x in range(1,1000):
        num = random.randrange(1,7)
        total += num

    print(total)


for _ in range(1001):
    dice()



