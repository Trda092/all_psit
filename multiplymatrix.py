""" multiply """


def multiply_matrix():
    """ multiply matrix """
    row, col, row2 = int(input()), int(input()), int(input())
    lst = []
    lst2 = []
    last = [[0 for i in range(row2)] for i in range(row)]
    for _ in range(row):
        ans = []
        for _ in range(col):
            ans.append(int(input()))
        lst.append(ans)
    for _ in range(col):
        ans = []
        for _ in range(row2):
            ans.append(int(input()))
        lst2.append(ans)
    for i in range(len(lst)):
        for j in range(len(lst2[0])):
            for k in range(len(lst2)):
                last[i][j] += lst[i][k]*lst2[k][j]
    _ = [print(*i, sep=" ") for i in last]


multiply_matrix()
