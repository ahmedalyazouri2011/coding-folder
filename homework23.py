
numbers = [x for x in range(1, 11)]
print("Numbers:", numbers)

even = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even)

odd = [x for x in numbers if x % 2 != 0]
print("Odd numbers:", odd)

squares = [x ** 2 for x in numbers]
print("Squares:", squares)

cubes = [x ** 3 for x in numbers]
print("Cubes:", cubes)

words = ["apple", "banana", "cherry"]
uppercase = [word.upper() for word in words]
print("Uppercase:", uppercase)
