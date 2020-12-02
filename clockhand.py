""" clockhands """
def clock(hour_line, minute_line):
    """ clockhands """
    hour_line = (hour_line*60+minute_line)*30/60
    minute_line = 6*minute_line
    print((hour_line >= minute_line and hour_line-minute_line <= 6))
clock(int(input()), int(input()))
