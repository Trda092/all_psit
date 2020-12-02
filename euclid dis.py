""" euclid dis """
def euclid_recur(lst, lst2):
    """ calculate """
    ans = ((lst[0]-lst2[0])**2+(lst[1]-lst2[1])**2)**0.5
    return ans
def main():
    """ main """
    plus = 0
    num = int(input())
    lst = []
    for _ in range(num):
        lst.append([int(i) for i in input().split()])
    for i in range(len(lst)-1):
        plus += euclid_recur(lst[i], lst[i+1])
    print("%.2f" %plus)
main()
