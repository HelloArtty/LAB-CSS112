def file_check():
    try:
        with open('myFile.txt', 'r') as file_read:
            read_file = file_read.read()
        return f"{read_file} \nSuccessfully print content in myFile.txt"
    except FileNotFoundError:
        return "Unable to open file myFile.txt"


print(file_check())