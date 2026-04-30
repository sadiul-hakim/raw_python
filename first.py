# Learning Python
message = "Hi Sabina,\nHow is my son?"
print(len(message))
print(message[:])

# String Formatting
first_name = "Abu"
last_name = "Salman"
full_name = f"{first_name} {last_name}"
print(first_name+" "+last_name)
print(f"{first_name} {last_name}")

# String Method
# Everything in python is object, and they have methods
# Python is case sensitive
print(first_name.upper())
print(first_name.lower())
print(first_name.capitalize())
print(full_name.strip())
print(full_name.find("Sal"))
print(full_name.replace("Salman", "Sallu"))
print("Salman" in full_name)
