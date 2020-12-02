"""test"""
def main(num, count=0):
    """test"""
    for i in range(1, num+1):
        for j in range(2, int(num**0.5)+1):
            if i % (j**2) == 0:
                count += 1
                break
    print(num-count)
main(int(input()))
