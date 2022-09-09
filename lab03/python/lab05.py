def num(choice):
    if choice == 1:
        base = int(input("Please enter the base length : "))
        height = int(input("Please enter the height : "))
        area = 1/2*base*height
        return f"The area of triangle with base = {base} and height = {height} is {area}"
    elif choice == 2:
        width = int(input("Please enter the base width : "))
        length = int(input("Please enter the length : "))
        height = int(input("Please enter the height : "))
        cubic = width*length*height
        return f"The cubic volumn of width = {width} length = {length} and height = {height} is {cubic}"
    elif choice == 3:
        base = float(input("Please enter the base diameter : "))
        height = float(input("Please enter the height : "))
        conical = ((1/3)*(22/7)*((base/2)**2)*(height))
        return f"The conical volumn of cone with diameter = {base} and height = {height} is {conical}"
    else:
        return "Invalid Choice"

print("Please enter a choice for your selection:")
print("Enter 1 if you want to calculate the area of a triangle.")
print("Enter 2 if you want to calculate the volumn of a cubic.")
print("Enter 3 if you want to calculate the volumn of a cone.") 
print(num(int(input("Enter your choice here:"))))