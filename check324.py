""" cat """
def cat():
    """ cat """
    name = input()
    lst = []
    time = 1
    while name != "END":
        if time == 1:
            if name.count(", ") > 0:
                lst.extend(name.split(", "))
            else:
                lst.append(name)
            time = 0
        elif name == "IT'S A DOG" and time == 0:
            lst.pop(len(lst)-1)
        elif name.count(", ") > 0 and name != "IT'S A DOG" and time == 0:
            lst.extend(name.split(", "))
        elif name.count(", ") == 0 and name != "IT'S A DOG" and time == 0:
            lst.append(name)
        name = input()
    inds = []
    for i in range(len(lst)):
        inds.append([lst.index(lst[i])+1, lst[i]])
    lst_new = list(set(lst))
    lst_new.sort()
    ans = 0
    for i in lst_new:
        for j in range(len(inds)):
            if i == str(inds[j][1]):
                ans = inds[j][0]
        print(i, ans, lst.count(i))
cat()
