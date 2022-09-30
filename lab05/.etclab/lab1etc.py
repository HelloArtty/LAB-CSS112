def file_check():
    try:
        with open('myFile.txt', 'r') as file_read:
            print(file_read.read())
            print("Successfully print content in myFile.txt")
    except FileNotFoundError:
        print("Unable to open file myFile.txt ")
        
file_check()
