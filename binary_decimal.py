Binary_Number = input("Enter a binary number: ")

decimal = 0
power = 0

for num in Binary_Number[::-1]:
    if int(num) > 1:
        print("Invalid binary input!")
        exit()
    decimal += int(num) * 2 ** power
    power += 1

print("Decimal:", decimal)