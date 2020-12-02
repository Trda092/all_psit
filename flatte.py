""" flat """


def flat(string):
    """ flat """
    txt = ""
    for i in string:
        if i.isnumeric() or i == "-":
            txt += i
        else:
            txt += " "
    #print(txt)
    ans = ""
    num = []
    for j in txt:
        if not j.isspace():
            ans += j
        else:
            num.append(ans)
            ans = ""
    check = [int(i) for i in num if not i == ""]
    print(sorted(check, key=float, reverse=1))

flat(input())
