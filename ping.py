""" ping """
def time(snd):
    """ time """
    if snd[0:5] == "Reply":
        check = snd.find("time")
        check2 = snd.find("ms")
        tme = snd[check+4:check2]
    else:
        tme = "=-1"
    if tme[0] == "=":
        return int(tme[1:])
    elif tme[0] == "<":
        return int(tme[1:])-1
    # elif tme[0] == ">":
    #     return int(tme[1:])+1

def ping_func():
    """ ping """
    imp, space, ping, snd1, snd2, snd3, snd4 \
        = input(), input(), input(), input(), input(), input(), input()
    sent = 4
    recieve = 4
    if ping.count("[") > 0:
        check = ping.find("[")
        ping_num = ping[check+1:ping.find("]")]
    elif ping.count("[") == 0:
        check = ping.find(" ")
        ping_num = ping[check+1:len(ping)-23]
    if snd1 == "Request timed out." or snd1 == "General failure.":
        recieve -= 1
    if snd2 == "Request timed out." or snd2 == "General failure.":
        recieve -= 1
    if snd3 == "Request timed out." or snd3 == "General failure.":
        recieve -= 1
    if snd4 == "Request timed out." or snd4 == "General failure.":
        recieve -= 1
    most = max(time(snd1), time(snd2), time(snd3), time(snd4))
    minin = most
    for _ in range(4):
        if time(snd1) <= minin and time(snd1) != -1:
            minin = time(snd1)
        if time(snd2) <= minin and time(snd2) != -1:
            minin = time(snd2)
        if time(snd3) <= minin and time(snd3) != -1:
            minin = time(snd3)
        if time(snd4) <= minin and time(snd4) != -1:
            minin = time(snd4)
    print("Ping statistics for %s:" %ping_num)
    print("    Packets: Sent = %d, Received = %d, Lost = %d (%d" %(sent, recieve, \
        sent-recieve, ((sent-recieve)/sent)*100)+"%"+" loss),")
    if recieve > 0:
        avr = ((time(snd1)*(time(snd1) > 0)+time(snd2)*(time(snd2) > 0)+\
            time(snd3)*(time(snd3) > 0)+time(snd4)*(time(snd4) > 0))/recieve)
        print("Approximate round trip times in milli-seconds:")
        print("    Minimum = %dms, Maximum = %dms, Average = %dms" %(minin, most, avr//1))
    imp = ""
    space = ""
    print(space+imp)
ping_func()
