""" bus stop """
def doin(move, stay, rmv, get):
    """do """
    if int(move) == int(stay):
        rmv.append(move)
        get += 1
    return get
def take(check, station):
    """ take """
    for _ in range(station):
        txt = input().split()
        check.append([int(i) for i in txt])
    check.sort(key=lambda x: int(x[0]))
    return check
def bus(capacity, station):
    """ bus stop """
    capa_bus = []
    check = []
    count = 0
    get = 0
    check = take(check, station).copy()
    #print(check)
    # print(len(check[1]))
    for i in range(station):
        stay = int(check[i][0])
        count += 1
        rmv = []
        if count == 1:
            for j in range(1, len(check[i])):
                if len(capa_bus) == capacity:
                    break
                if int(check[i][j]) > int(stay):
                    capa_bus.append(check[i][j])
        else:
            for move in capa_bus:
                get = doin(move, stay, rmv, get)
            if len(rmv) > 0:
                for k in range(len(rmv)):
                    capa_bus.remove(rmv[k])
            #print(capa_bus, stay, i)
            for k in range(1, len(check[i])):
                if len(capa_bus) == capacity:
                    break
                if int(check[i][k]) > int(stay):
                    capa_bus.append(check[i][k])
    print(get+len(capa_bus))
bus(int(input()), int(input()))
