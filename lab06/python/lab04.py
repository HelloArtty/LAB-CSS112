def p4():
    user_input = input().split()
    ans = 0
    for i in user_input:
        if int(i) < 0:
            ans += 1
    print(ans)