""" amicable """
def amicable(check):
    """ amicable """
    text = []
    for j in range(1, int(check**0.5)+1):
        if check%j == 0:
            text.append(j)
            k_num = (check//j)
            if k_num not in text:
                text.append(k_num)
    return sum(text)-check
    #     if sum(text)-i in range(1, number+1):
    #         ans.append(i)
    # print(sum(ans))
def main():
    """ main """
    num = int(input())
    ans = 0
    for i in range(1, num+1):
        if i == amicable(amicable(i)) and i != amicable(i):
            ans += i+amicable(amicable(i))
    print(ans//2)
main()
