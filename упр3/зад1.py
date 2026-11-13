n = int(input("Въведете броя на числата: "))

max_number = int(input("Въведете число: "))

for i in range(n - 1):
    number = int(input("Въведете число: "))

    if number > max_number:
        max_number = number

print("Най-голямото число е:", max_number)