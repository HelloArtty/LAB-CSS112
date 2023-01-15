N = 100

# def Problem3(N):
#     primes = [num for num in range(1,N) if not[d for d in range(2, num) if not num%d]]
#     odd_dict_of_primes =  {k:v for (k,v) in (dict(enumerate(primes)).items()) if k % 2 != 0}
#     return odd_dict_of_primes



primes = [num for num in range(1,N) if not[d for d in range(2, num) if not num%d]]
odd_dict_of_primes =  {k:v for (k,v) in (dict(enumerate(primes)).items()) if k % 2 != 0}
print(odd_dict_of_primes)
