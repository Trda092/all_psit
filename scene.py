""" sceneswitch """
def scene():
    """ sceneswitch """
    time = []
    count = 0
    status = "off"
    light = "no"
    #check = 0
    while True:
        order = input()
        if order == "End":
            break
        if float(order) == 0:
            status = "on"
            light = "daylight"
        elif status == "on" and float(order) != 0:
            time.append(float(order))
            status = "off"
            #print(time)
        elif status == "off" and float(order) != 0 and len(time) != 0:
            if float(order)-time[0] <= 6 and light == "daylight":
                status = "on"
                light = "warmwhite"
                count += 1
                time.pop(0)
            elif float(order)-time[0] <= 6 and light == "warmwhite":
                status = "on"
                light = "daylight"
                time.pop(0)
            elif float(order)-time[0] > 6:
                status = "on"
                light = "daylight"
                time.pop(0)
        #print(time)
    print(count)
scene()
