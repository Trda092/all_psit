""" run """

def run(distance, people):
    """ run """
    ans = []
    inds = []
    for i in range(people):
        txt = input().split()
        ans.append((distance-(int(txt[1])))/int(txt[0]))
        inds.append([i+1, int(txt[0])])
    if ans.count(min(ans)) > 1:
        count = 0
        check = []
        for i in ans:
            if i == min(ans):
                check.append(count)
            count += 1
        new = []
        for i in check:
            new.append(inds[i])
        new.sort(key=lambda x: x[1], reverse=1)
        print(new[0][0])
    else:
        print(ans.index(min(ans))+1)
run(int(input()), int(input()))
