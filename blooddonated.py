""" blood """


def blood():
    """ blood donated """
    age = int(input())
    if age in range(17, 71):
        weight = int(input())
        if weight >= 45:
            time = int(input())
            check = (time == 0)*(age <= 55)+(time > 0)
            if check == 1:
                if age == 17 or age in range(60, 71):
                    injured = input()
                    if injured == 'True':
                        return print("Yes")
                    else:
                        return print("No")
                else:
                    return print("Yes")
            else:
                return print("No")
        else:
            return print("No")
    else:
        return print("No")


blood()
