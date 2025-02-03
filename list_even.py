list = []

while(1):
    char = input("Enter the number to be entered in the list.\nIf you want to stop entering the number type \"n\": ")
    if char == 'n':
        break
    elif char.isdigit():
        list.append(int(char))
    else:
        print("Enter a valid Option")

even_list = [num for num in list if num%2==0]
even_list.sort()
print("New sorted list with the even number are:",even_list)