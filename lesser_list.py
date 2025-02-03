master = []
while(1):
    char = input("Enter the number to be entered in the list.\nIf you want to stop entering the number type \"n\": ")
    if char == 'n':
        break
    elif char.isdigit():
        master.append(int(char))
    else:
        print("Enter a valid Option")

number = int(input("Enter the number:"))

new_list = [num for num in master if num < number]
print("List with number smaller than ", number , "is", new_list)