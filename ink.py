""" ink """
def ink():
    """ ink """
    import math
    txt = input().split()
    for _ in range(int(txt[1])):
        point = input().split()
        rdis = ((int(point[0])-0)**2+(int(point[1])-0)**2)**(1/2)
        area = 3.1416*(rdis**2)
        print(math.ceil(area/int(txt[0])))
ink()
