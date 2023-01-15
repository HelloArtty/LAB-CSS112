N = 100

# def Reduce_this_to_NestedListComprehension(N):
#     primes = []
#     for num in range(1,N):
#         list_of_divisables = []
#         for d in range(2,num):
#             if num%d == 0: #divisable by some number
#                 list_of_divisables.append(d)
#         if not list_of_divisables:
#             primes.append(num)
#     return primes      

def Problem2(N):
    primes = [num for num in range(1,N) if not[d for d in range(2, num) if not num%d]]
    return primes

print(Problem2(N))



# print(list_of_divisables) #[3, 9, 11, 33]

# primes1 = [num for num in range(1,N) if all(num%d !=0 for d in range (2,num))]

# primes2 = [num for num in range(1,N) if 0 not in [num%d for d in range(2, num//2+1)]]

# primes3 = [num for num in range(1,N) if not[d for d in range(2, num) if not num%d]]

# print(primes1)
# print(primes2)
# print(primes3)