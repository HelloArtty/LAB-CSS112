def celsius(first_num, last_num):
    if first_num == last_num:
        return print(first_num, " Celcius = ", (1.80*first_num)+32, " Farenheit.")
    else:
        farenheit = float(1.80*first_num)+32.00
        print(first_num, " Celcius = %.2f Farenheit." % farenheit)
        return celsius(first_num+1, last_num)


first_num = int(input("Enter a beginning Celcius value: "))
last_num = int(input("Enter an ending Celeius value: "))
celsius(first_num, last_num)

