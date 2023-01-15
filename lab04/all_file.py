#1
def name (first_name,last_name):
    f_name = first_name
    l_name = last_name
    def fname_lname ():
        return  f"Hi, {f_name} {l_name}!"
    return fname_lname()

first_name = input("What is your name? : ")
last_name = input("What is your last name? : ")

print(name(first_name, last_name))

#2
def celsius(first_num,last_num):
    if first_num == last_num:
        return print(first_num," Celsius = ", (1.80*first_num)+32 ," Fahrenheit.")
    else:
        fahrenheit = float(1.80*first_num)+32.00
        print(first_num, " Celsius = %.2f Fahrenheit."%fahrenheit)
        return celsius(first_num+1,last_num)

first_num = int(input("Enter a beginning Celsius value: "))
last_num = int(input("Enter an ending Celsius value: "))
celsius(first_num,last_num)


#3
def multi_table(number,time):
    if time <= 12:
        Multiplication = number * time
        print("%d X %d = %d"%(number,time,Multiplication))  
        return multi_table(number,time+1)
    
number = int(input("Enter a number:"))
print("Multiplication Table of %d is:"%number)
multi_table(number,1)

#4
member_list = ["Tony", "Peter", "Mark", "Kim", "James", "Kenny" ]
def member_check(name, age) :
    def age_check():
            if age < 15:
                return True
            else:
                return False
    if name in member_list:
        if age_check() == True:
            return print("Ticket price for {} is: $ {} ".format(name, 15.0*0.25))
        else:
            return print("Ticket price for {} is: $ {} ".format(name, 15.0*0.5))
    else:
        if age_check() == True:
            return print("Ticket price for {} is: $ {} ".format(name, 15.0*0.5))
        else:
            return print("Ticket price for {} is: $ {} ".format(name, 15.0))

name = input("Please enter your name : ").capitalize()
age = int(input("Please enter your age : "))
member_check(name, age)
