""" bus stop """
def bus(capacity, station):
    """ bus stop """
    capa_bus = []
    count = 0
    get = 0
    for _ in range(station):
        txt = input().split()
        stay = int(txt[0])
        count += 1
        rmv = []
        if count == 1:
            for j in range(1, len(txt)):
                if len(capa_bus) == capacity:
                    break
                if int(txt[j]) >= int(stay):
                    capa_bus.append(txt[j])
        else:
            for i in capa_bus:
                if int(i) == int(stay):
                    rmv.append(i)
                    get += 1
            if len(rmv) > 0:
                for k in range(len(rmv)):
                    capa_bus.remove(rmv[k])
            for j in range(1, len(txt)):
                if len(capa_bus) == capacity:
                    break
                if int(txt[j]) >= int(stay):
                    capa_bus.append(txt[j])
        print(capa_bus)
        print(get+len(capa_bus))
bus(int(input()), int(input()))
