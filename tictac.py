""" tic tac """


def ttt():
    """ tic tac """
    lst = []
    for _ in range(3):
        lst.append([i for i in input()])
    # print(lst)
    if (lst[0][0] == lst[1][1] == lst[2][2] and \
        lst[0][0] != '-' and lst[1][1] != '-' and lst[2][2] != '-')\
         or (lst[0][2] == lst[1][1] == lst[2][0] and lst[0][2] != '-' \
             and lst[1][1] != '-' and lst[2][0] != '-'):
        print(lst[1][1], "WIN")
    else:
        for j in range(3):
            if lst[0][j] == lst[1][j] == lst[2][j] and\
                 (lst[0][j] != '-' and lst[1][j] != '-' and lst[2][j] != '-'):
                print(lst[0][j], "WIN")
                break
            elif lst[j][0] == lst[j][1] == lst[j][2] and\
                 (lst[j][0] != '-' and lst[j][1] != '-' and lst[j][2] != '-'):
                print(lst[j][0], "WIN")
                break
        else:
            print("DRAW")


ttt()
