def p6(): 
    x = [int(i) for i in input().split()]
    y = [int(i) for i in input().split()]
    z = []
    for i in range(len(x)):
        z.append(x[i]*y[i])
    print(*z)