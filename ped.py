""" ped """
def ped(num):
    """ ped """
    gas_lst, check = [int(input()) for i in range(num)], int(input())
    gas = [i for i in gas_lst if i <= check]
    supercheck = sorted(gas.copy())
    gas_ = list(set(sorted(gas)))
    als = gas_.copy()
    # print(gas_)
    for _ in als:
        if supercheck.count(_) >= 2:
            gas_.append(_)
    # print(gas_)
    gas_.sort()
    # print(gas_)
    ans = []
    for i in range(len(gas_)-1):
        for k in range(i+1, len(gas_)):
            if gas_[i] + gas_[k] == check:
                ans.append([gas_[i], gas_[k]])
        # print(ans)
    plus = 0
    delete = []
    for j in ans:
        if j[1] not in delete and j[0] != j[1]:
            n_num = supercheck.count(j[1])
            plus += n_num*(supercheck.count(j[0]))
            delete.append(j[1])
        elif j[1] not in delete and j[0] == j[1]:
            n_num = supercheck.count(j[1])
            plus += n_num*(n_num-1)//2
            delete.append(j[1])
    print(plus)
ped(int(input()))
