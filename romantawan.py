'''ROMAN'''
def main(txt, ans=0):
    '''main function'''
    roman = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
    for i in range(len(txt)):
        if roman[txt[i - 1]] < roman[txt[i]] and i > 0:
            ans += roman[txt[i]] - 2 * roman[txt[i - 1]]
            continue
        ans += roman[txt[i]]
    print(ans)
main(input())