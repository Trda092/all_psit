'''numday'''
def numday():
    '''numday'''
    f_day, f_month, s_day, s_month = int(input()), int(input()), int(input()), int(input())
    lst_31 = [1, 3, 5, 7, 8, 10, 12]
    lst_30 = [4, 6, 9, 11]
    day = f_day
    if (f_month in lst_30 and not f_day not in range(1,31)) or \
        (f_month in lst_31 and not f_day not in range(1,32)) or (f_month == 2 and  f_day not in range(1, 29)):
        return print('Impossible')
    elif (s_month in lst_30 and not s_day not in range(1,31)) or \
        (s_month in lst_31 and not s_day not in range(1,32)) or (s_month == 2 and  s_day not in range(1, 29)):
        return print('Impossible')
    for i in range(f_month, s_month):
        if i in lst_30:
            day += 30
        if i in lst_31:
            day += 31
        if i == 2:
            day += 28
    return print(day+s_day)
numday()