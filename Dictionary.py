# Stores key-value pairs.
user = {
    "name": "John",
    "age": 25
}

user["city"] = "London"


print(user)

user.update({
    "age": 30
})

print(user)

user.pop("age")

print(user)

print(user['name'])
print(user.get('name'))
print(user.keys())
print(user.values())
print(user.items())

for key, value in user.items():
    print(key, value)
