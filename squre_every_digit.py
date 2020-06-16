#     Welcome. In this kata, you are asked to square every digit of a number.

# For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

# Note: The function accepts an integer and returns an integer

def square_digits(num):
    dig = [int(x) **2 for x in str(num)]
    dig = int("".join([str(x) for x in dig]))
    print(dig)


square_digits(9119)

# more efficient

def square_digits1(num):
    print(int(''.join(str(int(d)**2) for d in str(num))))


square_digits1(8118)