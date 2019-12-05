# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"

# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.


def high_and_low(numbers):
    arr_num = numbers.split(" ")
    high = int(arr_num[0])
    low = int(arr_num[0])
    for num in arr_num:
        num = int(num)
        if num >= high:
            high = num
        elif num <= low:
            low = num

    high = str(high)
    low = str(low)
    numbers = high + " " + low

    print(numbers)
    return numbers

high_and_low("-1 -1 -1")

# cleaner way

def high_and_low2(numbers):
    numbers = [int(x) for x in numbers.split(" ")]
    return str(max(numbers)) + " " + str(min(numbers))

def high_and_low3(numbers):
  n = map(int, numbers.split(' '))
  return "{} {}".format(max(n), min(n))