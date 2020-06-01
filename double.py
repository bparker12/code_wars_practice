# Given an array of integers, return a new array with each value doubled.

# For example:

# [1, 2, 3] --> [2, 4, 6]

# For the beginner, try to use the map method - it comes in very handy quite a lot so is a good one to know.

def double(int):
    new = []
    for num in int:
        new.append(num *2)
    print(new)

double([1, 2, 3])
double([2, 4, 6])