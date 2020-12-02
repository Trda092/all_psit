""" ped """
def ped(num):
    """ ped """
    gas, check = [int(input()) for i in range(num)], int(input())
    ped_mid_sq = gas.count(check/2)
    ped_other = [gas.count(i)*gas.count(check-i) for i in set(gas) if i < check/2]
    print(int(sum(ped_other)+(ped_mid_sq*(ped_mid_sq-1)*0.5)))
ped(int(input()))
