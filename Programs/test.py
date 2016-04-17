fw = open('testing.txt', 'w')

def test():
    n = 1
    open('testing.txt', 'a')
    fw.write(n)
    fw.close()
