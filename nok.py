"""nok"""


def main():
    """Main Function"""
    num = int(input())
    leg = int(input())
    rabbit = (leg-2*num)/(2)
    if int(rabbit) >= 0 and int(num-rabbit) >= 0 and int(rabbit)+int(num-rabbit) \
            == num and (leg % 2 == 0 or leg % 4 == 0 or leg % 6 == 0):
        print(int(rabbit), int(num-rabbit))
    else:
        print("Impossible")


main()
