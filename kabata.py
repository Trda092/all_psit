""" kabata """
def kabata(num_txt):
    """ kabata """
    for _ in range(num_txt):
        txt = input()
        if txt.count("baka") > 0:
            print("no")
            continue
        else:
            txt = txt.replace("bakka", "")
            txt = txt.replace("ka", "")
            txt = txt.replace("ba", "")
            txt = txt.replace("ta", "")
        if len(txt) == 0:
            print("yes")
        else:
            print("no")
kabata(int(input()))
