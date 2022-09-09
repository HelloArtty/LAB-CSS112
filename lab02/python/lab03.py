number = int(input('Enter a number to to make a multiplication table:'))
i = 1
sum = number
while i <= 12:
    sum = number * i
    print("%.0f X %.0f = %.0f"%(number,i,sum))
    i+=1