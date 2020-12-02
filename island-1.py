''' Island '''


def main():
    ''' Main function '''
    count = 0
    row, col = [int(i) for i in input().split()]
    board = list()

    for i in range(row):
        board.append([int(i) for i in input().split()])

    for i in range(row):
        for j in range(col):
            if board[i][j] == 1:
                scan_island(board, i, j)
                count += 1

    print(count)


def scan_island(board, i, j):
    ''' Scan for island, turn all connected parts -1 '''
    board[i][j] = -1
    around = ((-1, -1), (0, -1), (1, -1), (1, 0),
              (1, 1), (0, 1), (-1, 1), (-1, 0))

    for k in around:
        if i + k[0] < 0 or i + k[0] >= len(board) or j + k[1] < 0 or j + k[1] >= len(board[0]):
            continue
        if board[i + k[0]][j + k[1]] == 1:
            scan_island(board, i + k[0], j + k[1])


main()
