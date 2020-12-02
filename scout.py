""" scout """


def scout(num):
    """ scout """
    for _ in range(num):
        count_p = 0
        count_w = 0
        npq = [int(i) for i in input().split()]
        weight = [int(i) for i in input().split()]
        weight.sort()
        #print(weight)
        for j in range(npq[0]):
            count_p += 1
            count_w += weight[j]
            if count_p > npq[1] or count_w > npq[2]:
                count_p -= 1
                break
        print(count_p)


scout(int(input()))
