""" cat parade """
def cat(name):
    """ cat parade """
    lst_name = []
    time = 1
    while name != 'END':
        if time == 1:
            name.split(",")
            lst_name.append(name)
            time = 0
        elif name.count(",") == 0:
            lst_name.append(name)
            print(lst_name,"1")
        elif name.count(",") > 0:
            name.split(", ")
            lst_name.append(name)
            print(lst_name,"2")
        name = input()
cat(input().split(", "))