""" children """
def children(day, age, height):
    """ children """
    if day == "Children Day":
        if (age < 14 and height <= 140) or (age < 14 and height < 90):
            print("FREE")
        else:
            print("PAY")
    if day == "Senior Day":
        if (age >= 60) or (age < 14 and height < 90):
            print("FREE")
        else:
            print("PAY")
    if day == "Normal Day":
        if age < 14 and height < 90:
            print("FREE")
        else:
            print("PAY")
children(input(), float(input()), float(input()))
