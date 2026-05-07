numbers = [1, 2, 3, 4, 5]
numbers.insert(0, 10)
numbers.append(20)
# numbers.clear()
newN = numbers.copy()
# print(newN)
print(numbers.count(1))
print(numbers)
numbers.extend([30, 40, 50])
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
print(len(numbers))
print(numbers[0:3])

for num in numbers:
    print(num)

nums = [1, 2, 3]

print(2 in nums)

nums = [1, 2, 3, 4]

squared = [x * x for x in nums]

print(squared)

users = [
    {"name": "John", "age": 20},
    {"name": "Alice", "age": 25}
]

print(users[0]["name"])
