#1
celsius = input('Please enter the temperature in Celsius : ') ;celsiusnum = int(celsius) ;fahrenheit = (9/5*celsiusnum)+32 ;print("The %.1f Celcius = %.1f Farenhite"%(celsiusnum,fahrenheit))

#2
number = int(input('Enter number '))
i = 0
sum = 0
while i <= number:
    sum = sum + i
    i+=1
print("Summation of numbers from 1 to %.0f is: %.0f"%(number,sum))


#3
number = int(input('Enter a number to to make a multiplication table:'))
i = 1
sum = number
while i <= 12:
    sum = number * i
    print("%.0f X %.0f = %.0f"%(number,i,sum))
    i+=1
    
    
#4
score = int(input('Please enter your score: '))

if score >= 80:
    gade ='A'
elif score < 80 and score >= 75:
    gade ='B+'
elif score < 75 and score >= 70:
    gade ='B'
elif score < 70 and score >= 65:
    gade ='C+'
elif score < 65 and score >= 60:
    gade ='C'
elif score < 60 and score >= 55:
    gade ='D+'
elif score < 55 and score >= 50:
    gade ='D'
elif score < 50:
    gade ='F'

print ("You got %s"%gade)


#5
start = int(input("Please enter a starting number:"))
end = int(input("Please enter an ending number:"))
print("\nPrime numbers between %.0f and %.0f are: "%(start,end))

for num in range(start,end):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            print(num)