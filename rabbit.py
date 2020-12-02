""" rabbit """


def rabbit():
    """ rabbit """
    num_rabbit = int(input())
    jump = int(input())
    num_carrot = int(input())
    # print(lst_rabbit)
    if jump >= num_rabbit*(num_rabbit+1)//2 and num_carrot >= num_rabbit:
        num_carrot = num_carrot-num_rabbit
        jump -= num_rabbit*(num_rabbit+1)//2
        num_rabbit = 0
    elif jump >= num_rabbit*(num_rabbit+1)//2 and num_carrot < num_rabbit:
        num_rabbit = num_rabbit-num_carrot
        jump -= num_carrot*(num_carrot+1)//2
        num_carrot = 0
    else:
        for j in range(min(num_rabbit, num_carrot), 0, -1):
            if j*(j+1)//2 <= jump and num_carrot >= num_rabbit:
                num_carrot -= j
                num_rabbit -= j
                jump -= j*(j+1)//2
                break
            elif j*(j+1)//2 <= jump and j <= num_carrot and num_carrot < num_rabbit:
                num_rabbit -= j
                num_carrot -= j
                jump -= j*(j+1)//2
                break
    if num_rabbit == 0 and num_carrot == 0 and jump == 0:
        print("Ahhahaha")
    else:
        print(num_rabbit, jump, num_carrot, sep=" ")


rabbit()
