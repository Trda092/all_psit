""" one two """
def one_two(num):
    """ one two """
    if num == 2:
        return "2"
    elif num == 1:
        return "1"
    else:
        return one_two(num-1)+one_two(num-2)
print(one_two(int(input())))
