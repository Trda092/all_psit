""" hwdotE """


def hwdote():
    """ hwdote """
    import math as m
    num = int(input())
    if num <= 2:
        print(2)
    else:
        if num % 2 != 0:
            print(int(2*m.factorial(num) /
                      ((m.factorial(num//2))*(m.factorial(num-num//2)))))
        else:
            print(int(2*m.factorial(num-1)/((m.factorial((num-1)//2))
                                            * (m.factorial((num-1)-(num-1)//2)))))


hwdote()
