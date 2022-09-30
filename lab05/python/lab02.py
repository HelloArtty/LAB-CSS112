def word_check():
    with open('myFile.txt', 'r') as file_read:
        word = len(file_read.read().strip())
        return f"Total letters are {word}"


print(word_check())