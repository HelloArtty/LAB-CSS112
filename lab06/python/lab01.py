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