""" main """
def main(num):
    """ main """
    if num > 1:
        main(num//2)
    print(num%2, end="")
main(int(input()))

