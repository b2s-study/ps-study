import sys

# 결과 출력
def print_the_sudoku(sudoku):
    for rows in sudoku:
        print(*rows)

def dfs(n):
    if n == blanks_count:
        print_the_sudoku(sudoku)
        exit(0)
    # row, col
    y, x = blanks[n]
    for i in range(1, 10):
        if not row_check[y][i] and not col_check[x][i] and not box_check[y // 3 * 3 + x // 3][i]:
            row_check[y][i] = col_check[x][i] = box_check[x // 3 + y // 3 * 3][i] = True
            sudoku[y][x] = i
            dfs(n + 1)
            row_check[y][i] = col_check[x][i] = box_check[x // 3 + y // 3 * 3][i] = False
            sudoku[y][x] = 0


if __name__ == "__main__":
    row_check = [[False] * 10 for j in range(10)]
    col_check = [[False] * 10 for j in range(10)]
    box_check = [[False] * 10 for j in range(10)]

    sudoku = [list(map(int, sys.stdin.readline().rstrip('\n').split())) for i in range(9)]

    blanks = []

    for i in range(9):
        for j in range(9):
            if not sudoku[i][j]:
                blanks.append((i, j))
            else:
                row_check[i][sudoku[i][j]] = True
                col_check[j][sudoku[i][j]] = True
                box_check[i // 3 * 3 + j // 3][sudoku[i][j]] = True
    blanks_count = len(blanks)
    dfs(0)