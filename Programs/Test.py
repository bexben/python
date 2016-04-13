from time import time, sleep, asctime
from tabulate import tabulate

x = 0

def timeming(n):

    global x
    x += 1

    table = [[n, x]]
    print(tabulate(table))

    sleep(1)

x = 1

for x in range(0,10):
    timeming(asctime())

