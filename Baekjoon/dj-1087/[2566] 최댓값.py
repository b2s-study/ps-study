import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

max_number = 0
for row in board:
  line_max_number = max(row)
  max_number = max(max_number, line_max_number)

for i in range(len(board)):
  if max_number not in board[i]:
    continue
  row_number = i + 1
  col_number = board[i].index(max_number) + 1

print(max_number)
print(row_number, col_number)
