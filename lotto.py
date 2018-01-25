import random
from numpy import genfromtxt

origin = range(1, 46)
data = []

def read_data():
    global data
    data = genfromtxt('lodata.csv', delimiter=',')


def logic():
    nums = origin[:]
    popped = []
    toCompare = [3, 8, 19, 27, 30, 41]
    count = 0
    while(toCompare != popped):
        nums = origin[:]
        popped = []
        for i in range(0, 6):
            popped.insert(0, nums.pop(random.randint(0, len(nums)-1)))
        popped.sort()
        count += 1

    print popped
    print count


if __name__ == '__main__':
    read_data()
