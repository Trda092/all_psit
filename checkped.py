""" ped """
import random
def ped(gas, check):
    """ ped """
    x_lst = gas.copy()
    for j in x_lst:
        if j > check:
            gas.remove(j)
    gas.sort()
    #print(len(gas))
    ans = []
    for i in range(len(gas)-1):
        first = gas[i]
        for k in range(i+1, len(gas)):
            if first + gas[k] == check:
                ans.append([first, gas[k]])
    return len(ans)
def ped2(lis ,check):
    '''main function'''
    ans=0
    lis2 = list(set([i for i in lis if i <= check*2]))
    for i in range(len(lis2)):
        for j in range(i+1, len(lis2)):
            if lis2[i] + lis2[j] == check:
                ans += lis.count(lis2[j]) * lis.count(lis2[i])
    #print(lis)
    return ans + (check==0) * lis.count(0)
def main():
    while True:
        gas_ped, check = [random.randrange(0, 100) for i in range(30)], 60
        gas = [i for i in gas_ped if i <= check]
        gas.sort()
        print(gas)
        if ped(gas_ped, check) != ped2(gas_ped, check):
            print(ped(gas_ped, check), ped2(gas_ped, check))
            break
main()