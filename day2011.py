""" day 2011 """
def day_2011(day, month):
    """ day 2011 """
    what_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    t_31 = [1, 3, 5, 7, 8, 10, 12]
    t_30 = [4, 6, 9, 11]
    inds_day = 5
    for i in range(1, month):
        if i in t_31:
            inds_day += 31
        elif i in t_30:
            inds_day += 30
        elif i == 2:
            inds_day += 28
    print(what_day[(inds_day+day)%7-1])
day_2011(int(input()), int(input()))
