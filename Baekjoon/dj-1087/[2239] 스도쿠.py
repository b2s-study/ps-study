import sys


def get_group_idx(row, col) -> int:
    return row // 3 * 3 + col // 3


def update_state(row, col, number, undo=False):
    global row_numbers, col_numbers, group_numbers

    state = False if undo == True else True
    row_numbers[row][number] = state
    col_numbers[col][number] = state
    gid = get_group_idx(row, col)
    group_numbers[gid][number] = state


def is_valid(row, col, number):
    global row_numbers, col_numbers, group_numbers
    if row_numbers[row][number] or col_numbers[col][number]:
        return False

    gid = get_group_idx(row, col)
    if group_numbers[gid][number]:
        return False

    return True


def simulate(row, col):
    # print(row, col)
    global sudoku
    # print("==============", blanks)
    # for li in sudoku:
    #     print(li)
    if row == 9:
        return True

    if sudoku[row][col] != 0:
        nrow = row + (col + 1) // 9
        ncol = (col + 1) % 9
        return simulate(nrow, ncol)

    for number in range(1, 10):
        if is_valid(row, col, number):
            sudoku[row][col] = number
            update_state(row, col, number)

            nrow = row + (col + 1) // 9
            ncol = (col + 1) % 9
            complete = simulate(nrow, ncol)
            if complete:
                return True

            sudoku[row][col] = 0
            update_state(row, col, number, undo=True)

    return


input = sys.stdin.readline

sudoku = [list(map(int, list(input().rstrip()))) for _ in range(9)]

row_numbers = [[True] + [False] * 9 for _ in range(9)]
col_numbers = [[True] + [False] * 9 for _ in range(9)]
group_numbers = [[True] + [False] * 9 for _ in range(9)]
blanks = set()
for row in range(9):
    for col in range(9):
        number = sudoku[row][col]
        update_state(row, col, number)


simulate(0, 0)
for li in sudoku:
    print("".join(map(str, li)))
