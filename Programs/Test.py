from time import sleep, asctime
from tabulate import tabulate

#Last updated by commit date; April 14


operatingTime = 0

#Creating txt record
fw = open('')

def timing(n):

    global operatingTime
    operatingTime += 1

    table = [[n, operatingTime]]
    print(tabulate(table))

    sleep(1)

operatingTime = 1

for operatingTime in range(0,10):
    timing(asctime())

