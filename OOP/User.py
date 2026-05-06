from abc import ABC, abstractmethod
from dataclasses import dataclass

# In python : Everything is Object
# No Method Overloading


class Address:
    pass


class User(ABC):
    def __init__(self, name):  # Constructor is __init__
        self.name = name
        address = Address()  # composition
        # Python does not enforce access control

    def sayHi(self):
        print("Hi This is User")

    @abstractmethod
    def work():
        pass

    @staticmethod
    def login():
        print("Logging in")

    def __str__(self):
        return f"User[name:{self.name}]"

    def __del__(self):
        print("Destroyed")


# NormalUser extended User
# Python supports multiple inheritance
class NormalUser(User):
    def sayHi(self):
        print("This is Normal User")

    def work():
        print("Working")


@dataclass
class Point:
    value: int
    date: str

# Dynamic nature


class A:
    pass


a = A()
a.new_field = "added later"

u = User("Hakim")  # No new keyword
print(u)
