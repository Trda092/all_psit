"""wpm"""
def kids(num):
    """ kids func """
    if num < 11:
        print('Very Slow')
    elif num in range(11, 21):
        print('Slow')
    elif num in range(21, 31):
        print('Average')
    elif num in range(31, 41):
        print('Fast')
    else:
        print('Very Fast')
def adult(num):
    """ adult fnc """
    if num < 26:
        print('Very Slow')
    elif num in range(26, 36):
        print('Slow/Beginner')
    elif num in range(36, 46):
        print('Intermediate/Average')
    elif num in range(46, 66):
        print('Fast/Advanced')
    elif num in range(66, 81):
        print('Very Fast')
    else:
        print('Insane')
def wpm():
    """ wpm """
    gen = input()
    num = int(input())
    if gen == 'Kids':
        kids(num)
    else:
        adult(num)
wpm()
