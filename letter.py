""" letter frequency """


def letter(txt):
    """ letter frequency """
    lst = []
    ans = []
    for i in txt:
        if i not in lst and i.isalpha():
            lst += [i]
    for i in lst:
        ans.append([i, txt.count(i)])
    ans.sort(key=lambda x: x[1], reverse=1)
    print(ans[0][0])


letter(input().lower())
