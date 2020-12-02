"""fibonucchi"""
def fibonacci(number, fibo_1, fibo_2):
    """fibonucchi"""
    if number > 0:
        fibo_2 = fibo_2+fibo_1
        fibo_1 = fibo_2-fibo_1
        number -= 1
    if number > 0:
        fibo_2 = fibo_2+fibo_1
        fibo_1 = fibo_2-fibo_1
        number -= 1
    if number > 0:
        fibo_2 = fibo_2+fibo_1
        fibo_1 = fibo_2-fibo_1
        number -= 1
    if number > 0:
        fibo_2 = fibo_2+fibo_1
        fibo_1 = fibo_2-fibo_1
        number -= 1
    if number > 0:
        fibo_2 = fibo_2+fibo_1
        fibo_1 = fibo_2-fibo_1
        number -= 1
    if number > 0:
        fibo_2 = fibo_2+fibo_1
        fibo_1 = fibo_2-fibo_1
        number -= 1
    if number > 0:
        fibo_2 = fibo_2+fibo_1
        fibo_1 = fibo_2-fibo_1
        number -= 1
    if number > 0:
        fibo_2 = fibo_2+fibo_1
        fibo_1 = fibo_2-fibo_1
        number -= 1
    if number > 0:
        fibo_2 = fibo_2+fibo_1
        fibo_1 = fibo_2-fibo_1
        number -= 1
    if number > 0:
        fibo_2 = fibo_2+fibo_1
        fibo_1 = fibo_2-fibo_1
        number -= 1
    if number == 0:
        return print(fibo_2+fibo_1)
    fibonacci(number, fibo_1, fibo_2)
def main(number, fibo_1, fibo_2):
    """ main """
    if number == 0:
        print(fibo_1)
    elif number == 1:
        print(fibo_2)
    elif number == 2:
        print(fibo_2+fibo_1)
    else:
        fibonacci(number-2, fibo_1, fibo_2)
main(int(input()), 0, 1)

