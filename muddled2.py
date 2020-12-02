""" muddled """


def muddled():
    """ muddled """
    lst = []
    while 1:
        order = input()
        if order == "DONE":
            break
        elif order == "SOMETHING'S WRONG":
            lst.clear()
        elif order.count("Can't do:") > 0:
            lst.remove(order[order.index(":")+2:])
        elif order == "CLOSED":
            lst.clear()
            break
        else:
            if order[order.index('#')+1:] != "N":
                lst.insert(int(order[order.index('#')+1:]) -
                           1, order[:order.index('#')-1])
            else:
                lst.append(order[:order.index('#')-1])
        # print(lst)
    rvs = lst.copy()
    rvs.reverse()
    print("Full Course:", lst, "Reversed:", rvs)


muddled()
