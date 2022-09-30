def celsius(first_num, last_num):
    if first_num <= last_num:
        fahrenheit = (1.80*first_num)+32.00
        file.write(f"{first_num} Celsius = {fahrenheit:.2f} Fahrenheit.\n")
        celsius(first_num+1, last_num)


first_num = int(input("Enter a beginning Celsius value: "))
last_num = int(input("Enter an ending Celsius value: "))
file = open('multiply.txt', 'w')
celsius(first_num, last_num)