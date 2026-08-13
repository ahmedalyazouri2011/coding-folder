number = int(input("Enter a number: "))
power = int(input("Enter the power: "))

answer = 1
while power > 0:
    answer *= number
    power -= 1

print(answer)