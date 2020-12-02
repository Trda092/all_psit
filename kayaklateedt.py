""" kayak """
def kayak(num):
    """ kayak """
    people = input().split(" ")
    people_n = []
    num = 0
    for i in people:
        people_n.append(int(i))
    people_n.sort()
    #print(people_n)
    while len(people_n) != 2:
        lst = []
        people_n.sort()
        for i in range(1, len(people_n)):
            lst.append(people_n[i]-people_n[(i-1)])
        inds = lst.index(min(lst))
        num += min(lst)
        #print(lst)
        for j in range(len(people_n)):
            if people_n[j] == people_n[inds] or people_n[j] == people_n[inds+1]:
                people_n[j] = ""
        people_n.remove("")
        people_n.remove("")
        if len(people_n) == 2:
            break
        #print(people_n)
    print(num)
kayak(int(input()))
