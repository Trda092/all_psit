'''coupon'''
def coupon():
    ''' coupon '''
    money = float(input())
    a_lst = [float(i) for i in input().split()]
    b_lst = [float(i) for i in input().split()]
    price_a = price_b = dis_b = check = 0
    if money >= a_lst[1]:
        price_a = money-a_lst[0]
        check += 1
    if money >= b_lst[1]:
        dis_b = ((b_lst[0])/100)*money
        price_b = money-dis_b
        check += 2
    # print(price_a, price_b)
    if check == 0:
        print('Nope')
    elif check == 1:
        print(1, '%.1f' %price_a)
    elif check == 2:
        print(2, '%.1f' %price_b)
    else:
        if a_lst[0] != dis_b:
            ans = min(price_a, price_b)
            print('1'*(ans == price_a)+'2'*(ans == price_b), '%.1f' %ans)
        elif a_lst[0] == dis_b and a_lst[1] == b_lst[1]:
            print(1, '%.1f' %price_a)
        elif a_lst[0] == dis_b and a_lst[1] < b_lst[1]:
            print(1, '%.1f' %price_a)
        elif a_lst[0] == dis_b and a_lst[1] > b_lst[1]:
            print(2, '%.1f' %price_b)
coupon()
