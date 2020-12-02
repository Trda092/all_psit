""" discount"""


def discount():
    """ discount """
    plus = 0
    lst = []
    while True:
        num = input()
        if num == "ENTER":
            break
        else:
            lst.append(int(num))
            plus += int(num)
    if len(lst) == 5:
        check = 0
    elif len(lst) in range(6, 12):
        check = 1
    elif len(lst) in range(12, 20):
        check = 2
    else:
        check = 4+(len(lst)-20)//5
    for _ in range(check):
        plus -= min(lst)
        lst.remove(min(lst))
    print(plus)


discount()
