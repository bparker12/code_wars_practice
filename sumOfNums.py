# Given two integers a and b, which can be positive or negative, find the sum of all the numbers between including them too and return it. If the two numbers are equal return a or b.

# Note: a and b are not ordered!

# get_sum(1, 0) == 1   // 1 + 0 = 1
# get_sum(1, 2) == 3   // 1 + 2 = 3
# get_sum(0, 1) == 1   // 0 + 1 = 1
# get_sum(1, 1) == 1   // 1 Since both are same
# get_sum(-1, 0) == -1 // -1 + 0 = -1
# get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2


def get_sum(a, b):
    total_num = 0
    if a > b:
        num_range = list(range(b, a))
        num_range.append(a)
        # print(num_range)
        for num in num_range:
            total_num += num
        print(total_num)
    elif b > a:
        num_range = list(range(a, b))
        num_range.append(b)
        # print(num_range)
        for num in num_range:
            total_num += num
        print(total_num)
    elif a == b:
        print(a)


get_sum(5, -1)
get_sum(0, 4)

get_sum(1, 0)
get_sum(1, 2)
get_sum(0, 1)
get_sum(1, 1)
get_sum(-1, 0)
get_sum(-1, 2)
