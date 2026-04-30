def arraySum(arr):

    if arr == None:
        return None

    sum = 0
    for num in arr:
        sum += num
    return sum


print(arraySum([1, 2, 3, 4, 5]))
print(arraySum(None))


def increment(number=0, by=0):  # Optional parameter should come after required parameters
    return number + by


print(increment(2, by=1))


def multiply(*numbers):
    res = 1
    for x in numbers:
        res *= x
    return res


print(multiply(1, 2, 3, 4, 5))
