""" break password """


def break_password():
    """ break password """
    import hashlib
    txt = input().lower()
    for i in range(100000):
        check = (hashlib.sha512(("%05d" %i).encode())).hexdigest()
        if check == txt:
            print("%05d" %i)
            break


break_password()
