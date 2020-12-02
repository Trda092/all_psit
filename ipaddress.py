""" ip address """
def ipadd():
    """ ipadress """
    ip_num = input()
    ans = ''
    for i in ip_num:
        if i == '.':
            continue
        elif not i.isnumeric() or i == ' ':
            return print("Invalid IPv4 address ")
    if ip_num.count('.') != 3:
        return print("Invalid IPv4 address ")
    else:
        for i in ip_num.split('.'):
            if int(i) < 0 or int(i) > 255:
                return print("Invalid IPv4 address ")
            else:
                ans += '%d' %int(i)+'.'
    return print(ans[:len(ans)-1])
ipadd()
