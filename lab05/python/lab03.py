def word_check():
    with open('myFile.txt', 'r') as file_read:
        word = len(file_read.read().split())
        return f"Total words are {word}"


print(word_check())