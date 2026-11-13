n = int(input("Въведете броя на числата: "))

total = 0

for i in range(n):
    number = int(input("Въведете число: "))
    total += number

print("Сумата е:", total)