import random
import numpy as np
from numpy import genfromtxt

numSet = range(1, 46)
data = []

def read_data():
    global data
    data = genfromtxt('lodata.csv', delimiter=',', dtype=int)


def getRandCount(toCompare):
    nums = numSet[:]
    popped = []
    count = 0
    while(not np.array_equal(toCompare, popped)):
        nums = numSet[:]
        popped = []
        for i in range(0, 6):
            popped.insert(0, nums.pop(random.randint(0, len(nums)-1)))
        popped.sort()
        count += 1

    return count


if __name__ == '__main__':
    read_data()
    count = getRandCount(data[0])
    print count
