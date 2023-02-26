import sys

input = sys.stdin.readline

STAR = "*"

def draw_star(x, y, size):
	if size == 3:
		for row in range(x, x+3):
			for col in range(y, y+3):
				if (row - x == 1 and col - y == 1):
					continue

				board[row][col] = STAR

	else:
		next_size = size // 3
		for row in range(3):
			for col in range(3):
				if (row == 1 and col == 1):
					continue

				draw_star(x + (row * next_size), y + (col * next_size), next_size)

n = int(input().rstrip('\n'))
board = [[" "] * n for _ in range(n)]

draw_star(0, 0, n)

for line in board:
	print(''.join(line))
