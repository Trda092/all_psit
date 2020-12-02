""" roman """


def roman(txt):
    """ roman """
    check = [['M', 1000], ['D', 500], ['C', 100], ['L', 50], ['X', 10], ['V', 5], ['I', 1]]
    special = [['CM', 900], ['CD', 400], ['XC', 90], ['XL', 40], ['IX', 9], ['IV', 4]]
    plus = 0
    count = 0
    for i in special:
        count = txt.count(i[0])
        txt = txt.replace(i[0], " ")
        plus += count*i[1]
    for j in check:
        count = txt.count(j[0])
        txt = txt.replace(j[0], " ")
        plus += count*j[1]
    #print(txt)
    print(plus)


roman(input())
