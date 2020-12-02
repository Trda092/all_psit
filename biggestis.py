''' Island '''
def main():
    ''' Main function '''
    row, col = [int(i) for i in input().split()]
    board = list()
    count = 0
    for i in range(row):
        board.append([int(i) for i in input().split()])
    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                count -= 1
                scan_island(board, i, j, count)
    mearg_board = []
    ans = []
    for i in board:
        mearg_board.extend(i)
    for i in range(count, 0):
        ans.append(mearg_board.count(i))
    print(max(ans))

def scan_island(board, i, j, count):
    ''' Scan for island, turn all connected parts -1 '''
    board[i][j] = count
    around = ((-1, -1), (0, -1), (1, -1), (1, 0),
              (1, 1), (0, 1), (-1, 1), (-1, 0))

    for k in around:
        if i + k[0] < 0 or i + k[0] >= len(board) or j + k[1] < 0 or j + k[1] >= len(board[0]):
            continue
        if board[i + k[0]][j + k[1]] == 1:
            scan_island(board, i + k[0], j + k[1], count)
main()
