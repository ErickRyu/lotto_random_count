import random
import numpy as np
from numpy import genfromtxt

numSet = range(1, 46)

def read_data():
    return genfromtxt('lodata.csv', delimiter=',', dtype=int)


def getRandCount(toCompare):
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
    data = read_data()
    count = getRandCount(data[0])
    print count
