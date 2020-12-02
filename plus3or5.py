""" divide 3 or 5 """
def main():
    """ divide """
    plus = 0
    for i in range(1, int(input())+1):
        if i%3 == 0 or i%5 == 0:
            plus += i
    print(plus)
main()

