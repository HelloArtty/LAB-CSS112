#1
def file_check():
    try:
        with open('myFile.txt', 'r') as file_read:
            read_file = file_read.read()
        return f"{read_file} \nSuccessfully print content in myFile.txt"
    except FileNotFoundError:
        return "Unable to open file myFile.txt"

print(file_check())

#2
def word_check():
    with open('myFile.txt', 'r') as file_read:
        word = len(file_read.read().strip())
        return f"Total letters are {word}"

print(word_check())

#3
def word_check():
    with open('myFile.txt', 'r') as file_read:
        word = len(file_read.read().split())
        return f"Total words are {word}"

print(word_check())

#4
def celsius(first_num,last_num):
    if first_num <= last_num:
        fahrenheit = (1.80*first_num)+32.00
        file.write(f"{first_num} Celsius = {fahrenheit:.2f} Fahrenheit.\n")
        celsius(first_num+1, last_num)

first_num = int(input("Enter a beginning Celsius value: "))
last_num = int(input("Enter an ending Celsius value: "))
file = open('multiply.txt', 'w')
celsius(first_num,last_num)
