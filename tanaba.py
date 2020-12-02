"""Tanabata"""

def main():
    """Solving"""
    text = input().split(".")
    maxx = max([len(i) for i in text])
    for j in text:
        j = str(j)+"_"*(maxx - len(j))
    for _ in range(len(text)):
        print("_|_",end=" ")
    print()
    # for i in range(maxx):
    #     for k in text:
    #         print("|%s|" % k[i],end=" ")
    #     print()
    print(text)
    
main()
