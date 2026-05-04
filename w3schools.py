import random

# print("Hi", end=",")
"""
print("Hi", 100, "Hello")
print("Hi", 100, "Hello")
print("Hi", 100, "Hello")
print("Hi", 100, "Hello")
num = 10
string = str(num)
print(string)
print(type(string))
"""

# Global

# If you create a variable with the same name inside a function, this variable will be local,
# and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
"""
x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)
"""
# To create a global variable inside a function, you can use the global keyword.

"""
def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
"""
# Also, use the global keyword if you want to change a global variable inside a function.
"""
x = 'awesome'


def myfunc():
    global x
    x = "fantastic"


myfunc()

print("Python is " + x)
"""
# Random

# print(random.randrange(1, 10))

# String
"""
for x in "banana":
    print(x)

print(len("banana"))

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

a = "Hello"
b = "World"
c = a + " " + b
print(c)

age = 22
print(f"Hakim is {age} years old")

price = 36.12345
print(f"Price : {price:.2f}")

name = "Hakim"
print(name.encode())
"""
