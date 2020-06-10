#Complete the square sum function so that it squares each number passed into it and then sums the results together.

#For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

def square_sum(numbers):
    total=0
    for num in numbers:
        total = (num * num) + total
    print(total)

square_sum([0, 3, 4, 5])

#another way to do it

def square_sum1(numbers):
    return sum(x ** 2 for x in numbers)
#the ** is the exponential, meaning it will multiply itself by the number specified. in this case its 2