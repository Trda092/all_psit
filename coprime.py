""" gcd """
def gcdv_1(a_num, b_num):
    """ gcd """
    if b_num == 0:
        return a_num
    else:
        return gcdv_1(b_num, a_num%b_num)
def main(num, num2):
    """ main """
    if gcdv_1(num, num2) == 1:
        print("YES")
        print(gcdv_1(num, num2))
    else:
        print("NO")
        print(gcdv_1(num, num2))
main(int(input()), int(input()))
