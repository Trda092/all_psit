""" semiprime """


def large_prime(num):
    """ large prime """
    import math as m
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num > 2 and num % 2 == 0:
        return False
    else:
        for i in range(3, m.floor(num**0.5)+1, 2):
            if num % i == 0:
                return False
        return True


def semiprime(num):
    """ semiprime """
    j_check = 0
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            j_check = num / i
            return large_prime(i) and large_prime(j_check)
    return False


def main():
    """ main """
    num = int(input())
    count = 0
    for i in range(1, num+1):
        if semiprime(i):
            count += 1
    print(count)


main()
