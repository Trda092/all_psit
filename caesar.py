""" caesar """
def caesar(num, txt):
    """ caesar """
    new = ""
    for i in txt:
        if i.upper().isalpha():
            new += chr((ord(i.upper())-65+num)%26+65)*(ord(i) in range(65, 91))+\
                (chr((ord(i.upper())-65+num)%26+65).lower())*(ord(i) not in range(65, 91))
        else:
            new += i
    print(new)
caesar(int(input()), input())
