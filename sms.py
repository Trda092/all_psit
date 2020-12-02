""" sms """
def sms():
    """ sms """
    lst = [[1, "DEL"], [2, "ABC"], [3, "DEF"], [4, "GHI"],\
     [5, "JKL"], [6, "MNO"], [7, "PQRS"], [8, "TUV"], [9, "WXYZ"]]
    time = int(input())
    new = ""
    for _ in range(time):
        button = int(input())
        press = int(input())
        txt = ""
        for j in lst:
            if button == j[0] and button != 1:
                txt += j[1][(press-1)%(len(j[1]))]
                new += txt
            elif button == j[0] and button == 1:
                new = new[:-1*press]
    if len(new) > 0:
        print(new)
    else:
        print("null")
sms()
