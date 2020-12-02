""" majority """


def major():
    """ majority """
    num_people = int(input())
    elec_card = int(input())
    ans = []
    lst = [int(input()) for _ in range(elec_card)]
    for i in range(1, num_people+1):
        ans.append([i, lst.count(i)])
    ans.sort(key=lambda x: x[1], reverse=1)
    if ans[0][1] > elec_card/2:
        print(ans[0][0], ans[0][1])
    else:
        print(0, ans[0][1])


major()
