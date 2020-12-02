""" horizontal """
def horizontal(txt):
    """ horizontal """
    lst = []
    for i in txt:
        if i not in lst:
            lst.append(i)
    lst.sort()
    cop_lst = lst.copy()
    #print(lst)
    ans = []
    for i in lst:
        if 64 < ord(i) < 91:
            ans.insert(1, i)
            cop_lst.remove(i)
    ans.sort()
    cop_lst.extend(ans)
    for i in cop_lst:
        if txt.count(i) > 5:
            answer = str(i)+" : "+"-----|"*((txt.count(i))//5)+"-"*((txt.count(i))%5)
            if txt.count(i)%5 == 0:
                print(answer[:len(answer)-1])
            else:
                print(answer)
        else:
            print(i, ":", "-"*((txt.count(i))))
horizontal(input())
