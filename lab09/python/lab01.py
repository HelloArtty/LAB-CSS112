def gen5odds():
    for i in range(0,100,10):
        nums = []
        x = i
        y = i + 10
        for j in range(x, y):
            if j % 2==1:
                nums.append()
    yield nums

def Problem1(): 
    return [sum(nums) for nums in gen5odds()]

# print(Problem1())
        
# print(gen5odds())

# def gen5odds():
#     for i in range(0,100,10):
#         yield list(j+i for j in range(10)  if j % 2==1)
# # print(gen5odds())
# def Problem1(): 
#     return [sum(j) for j in gen5odds()]
# print(Problem1())
    




# n = 100

# def odd(n):
#     nums = []
#     for i in range(1, n, 2):
#         nums.append(i)
#     return nums

# print(odd(n))
