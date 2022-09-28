def name (first_name,last_name):
    f_name = first_name
    l_name = last_name
    def fname_lname ():
        return  f"Hi, {f_name} {l_name}!"
    return fname_lname()

first_name = input("What is your name? : ")
last_name = input("What is your last name? : ")

print(name(first_name, last_name))