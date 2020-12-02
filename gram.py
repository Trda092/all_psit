import random
import string

def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    result_str = result_str.upper()
    return result_str

def gram(txt):
    """ gram """
    set_ = set()
    lst = []
    ans = []
    for i in range(1, len(txt)):
        set_.add((txt[i-1]+txt[i], i))
        lst.append(txt[i-1]+txt[i])
    #print(lst, set_)
    for i in sorted(set_, key=lambda x: x[1]):
        ans.append([i, lst.count(i[0])])
    most = max([i[1] for i in ans])
    #print(ans)
    for j in ans:
        if j[1] == most:
            return [j[0][0], j[1]]

def main(message):
    """main"""
    keep = dict()
    for i in range(len(message)-1):
        keep_j = message[i:i+2]
        if keep_j in keep:
            keep[keep_j] += 1
        else:
            keep[keep_j] = 1
    for i, j in keep.items():
        if j == max(keep.values()):
            return [i, j]



while True:
    used = get_random_string(20)
    print(used)
    if main(used) != gram(used):
        print(main(used), gram(used))
        break
    print(main(used), gram(used))

