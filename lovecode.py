"""Stamp"""

def main():
    """Main Function"""
    times = int(input())
    price_need = int(input())
    stamp_collect = int(input())
    stamp_use = int(input())
    discount = int(input())
    stamp = pay = 0
    for _ in range(times):
        price = int(input())
        while stamp >= stamp_use:
            stamp -= stamp_use
            price -= discount
            if price <= 0:
                price = 0
                break
        if price >= price_need:
            stamp += (price // price_need) * stamp_collect
        pay += price
    print(pay, stamp, sep="\n")

main()
