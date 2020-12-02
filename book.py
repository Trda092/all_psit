""" book """
def book():
    """ book """
    import math as m
    lem = int(input())
    page = int(input())
    x_num = int(input())
    y_num = int(input())
    lem_check = 0
    day = 0
    check = 0
    read = 0
    while lem_check < lem and read < page:
        read = m.ceil(((x_num + day) / (y_num + day)) * page)
        check += read
        if check >= page:
            lem_check += 1
            check = 0
        day += 1
    if lem_check != lem:
        day += lem - lem_check
    print(day)
book()
