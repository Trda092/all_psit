""" how many prime """
def howmanyprime(num):
    """ main """
    if num > 1:
        lst = [*(range(1, num+1))]
        lst.pop(0)
        check = lst.copy()
        for i in check:
            if (i % 2 == 0 and i != 2) or (i % 3 == 0 and i != 3) or (i % 5 == 0 and i != 5):
                lst.remove(i)
        print(len(lst))
    else:
        print("0")
howmanyprime(int(input()))
