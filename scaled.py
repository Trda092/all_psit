""" scale matrix """


def scale():
    """ scaled """
    num, num2 = int(input()), int(input())
    num_lst = []
    lst = []
    for _ in range(num):
        a_lst = []
        for _ in range(num2):
            inp = float(input())
            a_lst.append(inp)
            num_lst.append(inp)
        lst.append(a_lst)
    minim = min(num_lst)
    most = max(num_lst)
    for i in range(num):
        for j in range(num2):
            lst[i][j] = ("%.2f" %((lst[i][j]-minim)/(most-minim)))
    _ = [print(*i, sep=" ") for i in lst]

scale()
