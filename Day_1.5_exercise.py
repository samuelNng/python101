#Exercise 1: Create a function that takes two parameters for : name and age, and outputs a
#Birthday message “ Happy Birthday ‘name’ I hear you are ‘age’ today!”

def birthday_message(name, age):
#Generate a birthday message.
    message = "Happy Birthday " + name + "! I hear you are " + str(age) + " today!"
    return message

# Example usage:
name = "Alice"
age = 30
print(birthday_message(name, age))