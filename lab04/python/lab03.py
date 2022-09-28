def multi_table(number,time):
    if time <= 12:
        Multiplication = number * time
        print("%d X %d = %d"%(number,time,Multiplication))
        return multi_table(number,time+1)
    
number = int(input("Enter a number:"))
print("Multiplication Table of %d is:"%number)
multi_table(number,1)