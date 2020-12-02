""" class """


def classify():
    """ class """
    lst = []
    code_set = []
    while True:
        code = input()
        if code == "END":
            break
        lst.append(code)
        code_set.append(code[:4])
    code_sett = list(set(code_set))
    code_sett.sort()
    ans = []
    for j in code_sett:
        ans.append([str(j)[:2], str(j)[2:4], code_set.count(j[:4])])
    last = []
    for i in ans:
        if i not in last:
            last.append(i)
    count = 1
    check = []
    for i in last:
        if count == 1:
            print(i[0], int(i[1]), i[2])
            check += [i[0]]
            count = 0
        elif i[0] in check:
            print("--", int(i[1]), i[2])
        else:
            print(i[0], int(i[1]), i[2])
            check += [i[0]]


classify()
