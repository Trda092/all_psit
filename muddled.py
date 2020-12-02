""" muddled """
def muddled():
    """ muddled """
    rmv_lst = []
    ans = []
    while 1:
        order = input()
        if order == "DONE":
            break
        elif order == "SOMETHING'S WRONG":
            ans.clear()
        elif order.count("Can't do:") > 0:
            rmv_lst.append(order[order.index(":")+2:])
        elif order == "CLOSED":
            ans.clear()
            break
        else:
            ans.append([order[len(order)-1:], order[:len(order)-3]])
    lst = []
    lst_n = []
    #ans.sort(key=lambda x: x[0])
    for i in ans:
        if i[0] != "N":
            lst.insert(int(i[0]), i[1])
        else:
            lst_n.append(i[1])
    for i in lst_n:
        lst.append(i)
    for i in rmv_lst:
        lst.remove(i)
    print(ans, rmv_lst)
    print(lst)
muddled()
