""" 3nplus1 """
def n_plus(num, count):
    """ 3nplus1 """
    if num == 1:
        return count
    else:
        if num % 2 == 0:
            return n_plus(num//2, count + 1)
        else:
            return n_plus(num*3 + 1, count + 1)
def main():
    """ main """
    while True:
        number = int(input())
        if number == 0:
            break
        print(n_plus(number, 0)+1)
main()

