""" pongya """


def pongya():
    """ pongya """
    num = int(input())
    if num % 3 == 0 or str(num)[len(str(num))-1:] == '3':
        print("PONG")
    else:
        print(num)


pongya()
