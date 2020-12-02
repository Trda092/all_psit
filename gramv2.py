""" gramv2 """
def gram(txt):
    """ gram """
    set_ = set()
    lst = []
    ans = []
    for i in range(1, len(txt)):
        set_.add((txt[i-1]+txt[i], i))
        lst.append(txt[i-1]+txt[i])
    #print(lst, set_)
    for i in sorted(set_, key=lambda x: x[1]):
        ans.append([i, lst.count(i[0])])
    most = max([i[1] for i in ans])
    #print(ans)
    for j in ans:
        if j[1] == most:
            print(j[0][0])
            print(j[1])
            break
gram(input())
