""" main """
def func():
    """ main func """
    s = sorted({2, 6, 8})
    print(s)
    print(s[0])
    t = set(s)-set(list(set(set([s[0]]))))
    print(t)
func()
