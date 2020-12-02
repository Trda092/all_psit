""" is prime """
def prime_small():
    """ is prime """
    num = int(input())
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                print("No")
                break
        else:
            print("Yes")
    else:
        print("No")
prime_small()
