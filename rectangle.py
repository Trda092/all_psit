""" rectangle area """
def rectangle(a_point):
    """ rectangle """
    return [int(a_point[0]), int(a_point[1]), \
        int(a_point[0])+int(a_point[2]), int(a_point[1])+int(a_point[3])]
def main():
    """ main """
    lst_a = rectangle(input().split())
    lst_b = rectangle(input().split())
    x_num = set(range(lst_a[0], lst_a[2]+1)).intersection(set(range(lst_b[0], lst_b[2]+1)))
    y_num = set(range(lst_a[1], lst_a[3]+1)).intersection(set(range(lst_b[1], lst_b[3]+1)))
    if x_num == set() or y_num == set():
        print("no overlapping")
    else:
        del_x = max(x_num)-min(x_num)
        del_y = max(y_num)-min(y_num)
        print(del_x*del_y)
main()
