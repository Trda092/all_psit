""" hamming """
def hamming():
    """ hamming """
    string1, string2 = input(), input()
    ans = [i for i in range(len(string1)) if string1[i] != string2[i]]
    print(len(ans))
hamming()
