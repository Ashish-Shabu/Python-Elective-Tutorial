list_1 = list(map(int,input("Enter numbers in list 1 :").split()))
list_2 = list(map(int,input("Enter numbers in list 2 :").split()))


new_list = [num for num in list_1 if num in list_2]

print("Common numbers : ",new_list)