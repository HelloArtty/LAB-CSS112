###################################################################

#1

def p1():
    x=input().split() 
    c=input() 
    ans = []
    for i in range(len(x)):
        for n in x[i]:
            if c == n:
                try:
                    ans[i] += 1
                except:
                    ans.append(1)
    print(*ans)

###################################################################

#2

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

###################################################################

#3
def p4():
    user_input = input().split()
    ans = 0
    for i in user_input:
        if int(i) < 0:
            ans += 1
    print(ans)

###################################################################

#4
def p6(): 
    x = [int(i) for i in input().split()]
    y = [int(i) for i in input().split()]
    z = []
    for i in range(len(x)):
        z.append(x[i]*y[i])
    print(*z)

###################################################################
