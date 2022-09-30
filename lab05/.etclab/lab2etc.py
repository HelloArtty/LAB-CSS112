
def file_check(file):
        with open('myFile.txt', 'r') as file_read:
            word_count = 0
            for line in file_read:
                word_count += len(line)
            print("Total letters are = " + str(word_count))

file = ()
file_check(file)


def word_check():
    with open('myFile.txt', 'r') as file_read:
        word_count = 0
        for line in file_read:
            word_count += len(line)
        return f"Total letters are = {word_count}"

print(word_check())


def file_check(file):
    word_count = 0
    for line in file:
        word_count += len(line)
    print("Total letters are = " + str(word_count))

file = open('myFile.txt', 'r')
file_check(file)
file.close()


def word_check():
    with open('myFile.txt', 'r') as file_read:
        word = file_read.read().strip()
        letters = len(word)
        return f"Total letters are = {letters}"

print(word_check())

