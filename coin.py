""" coin change """
def coin():
    """ coin change """
    money = int(input())
    num_coin = 0
    if money >= 25:
        check_coin = money // 25
        money -= check_coin*25
        num_coin += check_coin
    if money >= 10:
        check_coin = money // 10
        money -= check_coin*10
        num_coin += check_coin
    if money >= 5:
        check_coin = money // 5
        money -= check_coin*5
        num_coin += check_coin
    if money >= 1:
        check_coin = money // 1
        money -= check_coin*1
        num_coin += check_coin
    print(num_coin)
coin()
