""" pairing number """
def pairnum():
    """ pairing number """
    a_list = [int(i) for i in input()[1:-1].split(", ")]
    b_list = [int(i) for i in input()[1:-1].split(", ")]
    plus_want = int(input())
    a_lst = [i for i in a_list if i <= plus_want]
    b_lst = [i for i in b_list if i <= plus_want]
    ans = 0
    for i in set(a_lst):
        ans += b_lst.count(plus_want-i)*(a_lst.count(i))
    print(ans)
pairnum()
