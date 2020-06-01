# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

# summation(2) -> 3
# 1 + 2

# summation(8) -> 36
# 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

def summation(num):
    sum = 0
    for x in range(num):
        sum = x + sum
    print (sum + num)

summation(8)

#best solution
def summation(num):
    return sum(range(1,num+1))