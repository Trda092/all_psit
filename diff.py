""" diff """


def dif():
    """ dif """
    from json import loads
    lst = loads(input())
    lst2 = loads(input())
    sett = set(lst)
    sett_2 = set(lst2)
    check = sett.union(sett_2)
    count = 0
    for i in sorted(check):
        if abs(lst.count(i)-lst2.count(i)) != 0:
            print(i, abs(lst.count(i)-lst2.count(i)))
            count += 1
    if count == 0:
        print("ONAJI DAYO!")


dif()
