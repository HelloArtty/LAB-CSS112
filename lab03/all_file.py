#1
list_name=['Jeff','Jack','Jim']

def check_name(name):
    if name in list_name:
        return f"Hello, {name}. Good morning my friend!"
    else:
        return f"Who are you? \nNice to meet you anyway...{name} :)."

print(check_name(input('What is your name? : ')))

#2
def calculator(hour,rate):
    if  hour <= 40:
        pay = hour*rate
        return f"{pay}"
        
    else:
        up_hour = hour - 40
        pay = (40*rate)+(up_hour*1.5*rate)
        return f"{pay}"

hour_work = int(input('How many hours did you work last week? :'))
rate_per_hour = int(input('What is yor pay rate per hour(between 10-25) :'))

print(calculator(hour_work,rate_per_hour))

#3
def prime_check(number):
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                return "This is not a prime number."
        else:
            return "This is a prime number"
    else:
        return "This is not a prime number."

print(prime_check(int(input('Enter a number to test:'))))

#4
list_number = []
num = int(input("Enter nuber of element : "))

for i in range(1, num + 1):
    number = int(input(""))
    list_number.append(number)
    
print("The entered list is ",list_number)
print("The maximum number entered is ",max(list_number))
print("The minimum number entered is ",min(list_number))

#5
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