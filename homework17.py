try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Age is not correct")
    elif age % 2 == 0:
        print("Your age is even")
    else:
        print("Your age is odd")

except:
    print("Please enter a valid age")