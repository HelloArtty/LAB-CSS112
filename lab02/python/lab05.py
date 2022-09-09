start = int(input("Please enter a starting number:"))
end = int(input("Please enter an ending number:"))
print("\nPrime numbers between %.0f and %.0f are: "%(start,end))

for num in range(start,end):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            print(num)