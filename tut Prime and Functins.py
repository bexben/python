
def prime(y):
    for x in range(2, 1000000000):
        z = y % x
        if z == 0 and y != x:
            print("Y is not prime")
            break
        elif x == 1000000000 or x == y:
            print("Y is prime")
        else:
            continue

prime(654188429)




