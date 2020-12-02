""" olympic """


def olympic(num):
    """ olympic """
    lst = []
    rank = 0
    count = 1
    for _ in range(num):
        selected = input().split()
        lst.append(selected)
    lst.sort(key=lambda x: x[0])
    lst.sort(key=lambda x: int(x[3]), reverse=1)
    lst.sort(key=lambda x: int(x[2]), reverse=1)
    lst.sort(key=lambda x: int(x[1]), reverse=1)
    # for i in range(3, 0, -1):
    #     lst.sort(key=lambda x: int(x[3]), reverse=1)
    check = []
    for j in range(len(lst)):
        plus = int(lst[j][1])+int(lst[j][2])+int(lst[j][3])
        if [int(lst[j][1]), int(lst[j][2]), int(lst[j][3])] not in check:
            rank += count
            check.append([int(lst[j][1]), int(lst[j][2]), int(lst[j][3])])
            count = 1
        else:
            rank += 0
            count += 1
        print(rank, lst[j][0], int(lst[j][1]),
              int(lst[j][2]), int(lst[j][3]), plus)


olympic(int(input()))
