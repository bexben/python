def addNums(*args):
    total = 0
    for x in args:
        total += x
    print(total)

nums = [1, 4, 10, 100]

addNums(nums[0], nums[1], nums[2]) #takes longer, doesnt work with flexible args because you need to input it
addNums(*nums) #better, works everywhere, less code
