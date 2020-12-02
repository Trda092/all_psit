""" gcd N """
def gcdv_1(a_num, b_num):
    """ gcd """
    if b_num == 0:
        return a_num
    else:
        return gcdv_1(b_num, a_num%b_num)
def main():
    """ main """
    reg = int(input())
    lst = [int(input()) for i in range(reg)]
    if len(lst) == 1:
        print(lst[0])
    else:
        gcd = gcdv_1(lst[0], lst[1])
        for i in range(2, len(lst)):
            gcd = gcdv_1(gcd, lst[i])
        print(gcd)
main()
