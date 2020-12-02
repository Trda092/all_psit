""" tax """
def tax():
    """ tax """
    year, motor = int(input()), int(input())
    price = 0
    if motor > 1800:
        price = 2100+(motor-1800)*4
    elif 600 < motor <= 1800:
        price = 300+(motor-600)*1.5
    elif 1 <= motor <= 600:
        price = motor*(0.5)
    ans = price*((1)*(year < 6)+(0.9)*(year == 6)+(0.8)*(year == 7)+\
        (0.7)*(year == 8)+(0.6)*(year == 9)+(0.5)*(year >= 10))
    print("%.2f" %ans)
tax()
