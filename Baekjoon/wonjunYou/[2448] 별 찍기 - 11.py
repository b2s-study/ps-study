import sys

input = sys.stdin.readline

STAR = "*"

n = int(input().rstrip('\n'))
board = [[' '] * 2 * n for _ in range(n)]

def draw_star(x, y, size):
    if size == 3:
        board[x][y] = STAR
        board[x + 1][y - 1] = STAR
        board[x + 1][y + 1] = STAR

        for idx in range(-2, 3):
            board[x + 2][y + idx] = STAR

        return

    else:
        half = size // 2

        draw_star(x, y, half)
        draw_star(x + half, y - half, half)
        draw_star(x + half, y + half, half)

draw_star(0, n - 1, n)
for line in board:
    print(''.join(line))