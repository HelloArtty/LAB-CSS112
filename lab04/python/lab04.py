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
