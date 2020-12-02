""" safe """
def baron(txt, txt2):
    """ safe """
    lst = []
    for i in range(65, 91):
        lst.append(chr(i))
    plus = 0
    for j in range(1, len(txt)+1):
        inds = lst.index(txt2[j-1])+1
        for k in range(1, j+1):
            inds2 = lst.index(txt[k-1])+1
        diff = abs((inds*(inds >= inds2)+inds2*(inds2 > inds))-(min(inds, inds2)+26))
        plus += min(abs(inds-inds2), diff)
    print(plus)
baron(input(), input())

