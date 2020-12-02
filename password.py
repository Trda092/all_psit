""" password """
def password():
    """ password """
    import hashlib
    txt = input()
    result = hashlib.sha512(txt.encode())
    print((result.hexdigest()).upper())
password()
