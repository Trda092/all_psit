""" caesar """
def caesar(txt):
    """ caesar """
    for i in range(-26, 27):
        new = ""
        for j in txt:
            if j.upper().isalpha():
                new += chr((ord(j.upper())-65+i)%26+65)*(ord(j) in range(65, 91))+\
                    (chr((ord(j.upper())-65+i)%26+65).lower())*(ord(j) not in range(65, 91))
            else:
                new += j
        if new.count("The")+new.count("the") > 0:
            print(new)
            break
caesar(input())
