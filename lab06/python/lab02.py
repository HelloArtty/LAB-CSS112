def p2():
    posneg = [int(i) for i in input().split()]
    noneg = []
    count = 0
    while count < len (posneg):
        if posneg[count] < 0:
            posneg.remove(posneg[count])
        else:
            count +=1
    noneg = posneg
    print(*noneg)