""" binary """
def twonary():
    """ binary """
    num = int(input())
    lst = 0
    for i in range(num):
        if 2**i >= num:
            lst = i
            break
    ans = ""
    for j in range(lst, -1, -1):
        check = 0
        while num >= 2**j:
            num -= 2**j
            check = 1
        ans += str(check)
    print(int(ans))
twonary()
