""" circular prime """


def isprime(num):
    """ num """
    import math as m
    if num == 2:
        status = True
    elif num > 2 and num % 2 == 0:
        status = False
    else:
        for i in range(3, m.floor(int(num**0.5))+1, 2):
            if num % i == 0:
                status = False
                break
        else:
            status = True
    return status


def check_cir(num):
    """ check """
    count = len(str(num))
    for _ in range(count):
        num = int(str(num)[1:]+str(num)[0])
        if not isprime(num):
            return False
    return True


def circular_prime(num):
    """ circular_prime """
    ans = []
    for i in range(2, num+1):
        if isprime(i):
            if str(i).count("0")+(str(i).count("2") and i != 2)+str(i).count("4")+\
                str(i).count("6")+str(i).count("8")+\
                (str(i).count("5") and i != 5) == 0:
                ans.append(i)
    #print(ans)
    for i in range(len(set(ans))):
        if not check_cir(ans[i]):
            ans.remove(ans[i])
            ans.insert(i, 0)
    print(sum(ans))


circular_prime(int(input()))
