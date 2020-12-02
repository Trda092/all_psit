""" ball """
def ball():
    """ balll """
    height = float(input())
    count = 0
    while height >= 0.01:
        height *= 0.6
        count += 1
    print(count-1)
ball()
