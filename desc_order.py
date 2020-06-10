# Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

# Examples:
# Input: 21445 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

def descending_order(num):
    num_list = [int(x) for x in str(num)]
    num_list.sort(reverse=True)
    num_list = "".join(str(x) for x in num_list)
    print(int(num_list))


# descending_order(145263)
# descending_order(15)
# descending_order(123456789)

#preferred way to solve problem:

def Descending_Order1(num):
    print(int("".join(sorted(str(num), reverse=True))))

Descending_Order1(145263)
Descending_Order1(21654984918948918919848978956156)