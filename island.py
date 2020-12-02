""" island """
def check_is(lst, i, j):
    """ check_is land """
    lst[i][j] == -1
    check = ((-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0))
    for k in check:
        if lst[i+k[0]][j+k[1]] == 1:
            check_is(lst, i+k[0], j+k[1])

def island(reg):
    lst = []
    count = 0
    for _ in range(int(reg[0])):
        txt = [int(i) for i in  input().split()]
        lst.append(txt)
    for i in range(int(reg[0])):
        for j in range(int(reg[1])):
            if lst[i][j] == 1:
                check_is(lst, i, j)
                count += 1
    print(count)
island(input().split())