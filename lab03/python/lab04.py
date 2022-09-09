list_number = []
num = int(input("Enter nuber of element : "))

for i in range(1, num + 1):
    number = int(input(""))
    list_number.append(number)
    
print("The entered list is ",list_number)
print("The maximum number entered is ",max(list_number))
print("The minimum number entered is ",min(list_number))