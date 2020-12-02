''' hint '''
def check(sym, num):
    ''' check '''
    if sym == '<':
        return [i for i in range(int(num))]
    if sym == '<=':
        return [i for i in range(int(num)+1)]
    if sym == '==':
        return [int(num)]
    if sym == '!=':
        return [i for i in range(10) if i != int(num)]
    if sym == '>=':
        return [i for i in range(int(num), 10)]
    if sym == '>':
        return [i for i in range(int(num)+1, 10)]
def hint():
    ''' hint '''
    sym_n, num_n = input().split()
    sym_t, num_t = input().split()
    sym_h, num_h = input().split()
    ans = []
    check_n, check_t, check_h = check(sym_n, num_n), check(sym_t, num_t), check(sym_h, num_h)
    # print(check_n, check_t, check_h)
    for i in check_h:
        for j in check_t:
            for k in check_n:
                ans.append("%03d" %(i*100+j*10+k))
    print(*ans, sep='\n')
hint()
