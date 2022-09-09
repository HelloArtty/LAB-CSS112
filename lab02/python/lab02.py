number = int(input('Enter number '))
i = 0
sum = 0
while i <= number:
    sum = sum + i
    i+=1
print("Summation of numbers from 1 to %.0f is: %.0f"%(number,sum))