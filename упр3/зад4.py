number = int(input("Въведете число: "))

if number <= 1:
    print("Числото не е просто.")
else:
    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Числото е просто.")
    else:
        print("Числото не е просто.")