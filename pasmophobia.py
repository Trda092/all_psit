""" pasmophobia """


def pasmophobia():
    """ pasmophobia """
    evd = input()
    ev2 = input()
    ev3 = input()
    item = [["EMF Level 5", "Banshee", "Jinn", "Oni", "Phantom", "Revenant", "Shade"],\
            ["Ghost Writing", "Demon", "Oni", "Revenant", "Shade", "Spirit", "Yurei"],\
            ["Fingerprints", "Banshee", "Poltergeist", "Revenant", "Spirit", "Wraith"],\
            ["Spirit Box", "Demon", "Jinn", "Mare", "Oni", "Poltergeist", "Spirit", "Wraith"],\
            ["Freezing Temperatures", "Banshee", "Demon", "Mare", "Phantom", "Wraith", "Yurei"],\
            ["Ghost Orb", "Jinn", "Mare", "Phantom", "Poltergeist", "Shade", "Yurei"],
            ["No evidence", "Banshee", "Demon", "Jinn", "Oni", "Mare", "Phantom", "Poltergeist",\
            "Revenant", "Shade", "Spirit", "Wraith", "Yurei"]]
    lst = []
    for i in item:
        if i[0] == evd:
            set_a = set(i[1:])
            lst.append(set_a)
        if i[0] == ev2:
            set_b = set(i[1:])
            lst.append(set_b)
        if i[0] == ev3:
            set_c = set(i[1:])
            lst.append(set_c)
    ans = set()
    if len(lst) == 3:
        ans = (lst[0].intersection(lst[1])).intersection(lst[2])
    if len(lst) == 2:
        ans = (lst[0].intersection(lst[1]))
    if len(lst) == 1:
        ans = lst[0]
    if ans == set():
        print("Not yet discovered")
    else:
        print(*sorted(ans), sep="\n")


pasmophobia()
