list_name=['Jeff','Jack','Jim']

def check_name(name):
    if name in list_name:
        return f"Hello, {name}. Good morning my friend!"
    else:
        return f"Who are you? \nNice to meet you anyway...{name} :)."

print(check_name(input('What is your name? : ')))