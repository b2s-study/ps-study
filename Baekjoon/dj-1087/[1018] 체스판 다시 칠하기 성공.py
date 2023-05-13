N, M = map(int, input().split())

board = [input() for _ in range(N)]
min_list = []

for row in range(0, N-7):
    for col in range(0, M-7):
        cnt_b = 0
        cnt_w = 0
        for i in range(row, row+8):
            for j in range(col, col+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'B':
                        cnt_b += 1
                    if board[i][j] != 'W':
                        cnt_w += 1
                else:
                    if board[i][j] != 'W':
                        cnt_b += 1
                    if board[i][j] != 'B':
                        cnt_w += 1
        min_list.append(cnt_b)
        min_list.append(cnt_w)
print(min(min_list))
