""" diamond """
def diamond(num):
    """ diamond """
    for i in range(num):
        if i == 0 or i == num-1:
            space = " "*((num-1)//2)
            print(space+"*"+space)
        elif ((num-1)//2) > i > 0:
            space = " "*((num-1)//2-i)
            n_space = " "*(2*i-1)
            print(space+"*"+n_space+"*"+space)
        elif i == ((num-1)//2):
            print("*"*num)
        elif i > ((num-1)//2):
            space = " "*(i-((num-1)//2))
            check = i-(i-((num-1)//2))*2
            n_space = " "*(check*2-1)
            print(space+"*"+n_space+"*"+space)
diamond(int(input()))
