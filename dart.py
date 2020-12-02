""" dart """
def dart(num):
    """ dart """
    import math as m
    lst = []
    ans = 0
    for _ in range(num):
        lst.append(list(map(float, input().split())))
    for i in lst:
        raeg = m.hypot(i[0], i[1])
        if raeg <= 2:
            ans += 5
        elif raeg <= 4:
            ans += 4
        elif raeg <= 6:
            ans += 3
        elif raeg <= 8:
            ans += 2
        else:
            ans += 1*(raeg <= 10)
    print(ans)
dart(int(input()))
