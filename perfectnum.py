""" perfect number """
def perfect(number):
    """ perfect number """
    ans = []
    for i in range(1, number+1):
        text = []
        for j in range(1, int(i**0.5)+1):
            if i%j == 0:
                text.append(j)
                k_num = (i//j)
                if k_num not in text:
                    text.append(k_num)
        if sum(text)-i in range(1, number+1):
            ans.append(i)
    print(sum(ans))
perfect(int(input()))
