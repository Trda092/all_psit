""" book worm """
def book_func():
    """ book worm """
    lst_time = []
    test_case = int(input())
    for _ in range(test_case):
        minute = float(input())
        book = int(input())
        read_time = 0
        read = 0
        for _ in range(book):
            time = float(input())
            lst_time.append(time)
        lst_time.sort()
        #print(lst_time)
        for i in range(book):
            read_time += lst_time[i]
            if read_time > minute:
                read_time -= lst_time[i]
            else:
                read += 1
        print(read)
        lst_time.clear()
book_func()
