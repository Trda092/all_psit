""" prosomsib """
def prasomsib():
    """ prasomsib """
    txt = input()
    pin = 0
    plus = 0
    for i in range(len(txt)):
        plus = int(txt[i])
        for j in range(i+1, len(txt)):
            plus += int(txt[j])
            if plus == 10:
                pin += 1
                #print(ans)
                break
    print(pin)
prasomsib()
