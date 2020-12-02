""" blackspace """
def blackspace(txt):
    """ blackspace """
    check = ""
    count = 0
    lst = []
    for i in txt:
        if i != "<" and count == 0:
            print("1")
            check += i
            print(check)
        elif i == "<":
            print("2")
            print(check)
            count += 1
        elif i != "<" and count > 0 and check != "":
            print("3")
            lst.append(check)
            count = 0
        print(lst)

blackspace(input())