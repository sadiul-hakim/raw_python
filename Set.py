# Set stores unique values only.

nums = {1, 2, 2, 3, 30, 6, 7, 8}
nums.add(10)
newNums = nums.union({10, 20})
print(nums)
print(newNums)
diff = nums.difference({2, 4, 5})
print(diff)
nums.discard(10)
inter = nums.intersection({1, 5, 7, 8})
print(inter)

setA = {1, 2, 3}
setB = {2, 3, 4}
print(setA | setB)  # Union, all unique items
print(setA & setB)  # Intersection, only items in common
