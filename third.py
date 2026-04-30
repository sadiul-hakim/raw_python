temperature = 35
if temperature > 30:
    print("Too Hot")
elif temperature > 20:
    print("Fine")
else:
    print("Nothing")

under_graduate = True
print("Focus on Study" if under_graduate else "Have Fun")

# and, or, not

age = 22
if 18 <= age < 35:
    print("Ok")

# Loops
for number in range(10):
    print(number)

print("---------------------")

for number in range(1, 5):
    print(number)

print("---------------------")

for number in range(1, 10, 2):
    print(number)

# break, continue
