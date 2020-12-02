""" how many prime """
def howmanyprime(num):
    """ main """
    lst = [i for i in range(1, num+1)]
    lst.pop(0)
    ans = []
    for i in lst:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            ans.append(i)
    print(len(ans))
howmanyprime(int(input()))
