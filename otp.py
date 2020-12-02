""" otp """
def otp():
    """ otp """
    num = input()
    while num != '0':
        dick = dict()
        for i in num:
            if i not in dick:
                dick.update({int(i):num.count(i)})
        if len(num) == 4:
            if len(dick) == 3:
                print("Valid")
            else:
                print("Invalid")
        if len(num) == 6:
            x_ans = list(dick.values())
            count2 = x_ans.count(2)
            count3 = x_ans.count(3)
            if (count2 == 2 and count3 == 0) or ((count2 == 0 or count2 == 1) and count3 == 1):
                print("Valid")
            else:
                print("Invalid")
        if len(num) == 8:
            x_ans = list(dick.values())
            count2 = x_ans.count(2)
            count3 = x_ans.count(3)
            if ((count2 == 0 or count2 == 1) and count3 == 2) or (count2 == 3 and count3 == 0):
                print("Valid")
            else:
                print("Invalid")
        num = input()
otp()
