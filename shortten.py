""" shortten """
def shortten(num):
    """ shortten """
    first = num
    r_first = num
    count = 0
    ans = ""
    while num != -1:
        if count == 0:
            first = num
            count += 1
        elif r_first+1 == num:
            count += 1
            r_first = num
        elif r_first+1 != num:
            if count > 1:
                ans += str(first)+"-"+str(r_first)+", "
            elif count == 1:
                ans += str(r_first)+", "
            count = 1
            r_first = num
            first = r_first
        num = int(input())
    if count > 1:
        ans += str(first)+"-"+str(r_first)
    elif count == 1:
        ans += str(r_first)
    print(ans)
shortten(int(input()))
