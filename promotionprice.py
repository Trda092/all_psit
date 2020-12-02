""" pro """
def pro():
    """ pro """
    promo_people, real_spend, price, real_people = int(input()), int(input()),\
         int(input()), int(input())
    ans = 0
    if real_people >= promo_people:
        ans += (real_people//promo_people)*real_spend*price
    ans += (real_people%promo_people)*price
    print(ans)
pro()
