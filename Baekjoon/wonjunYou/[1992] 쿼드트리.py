import sys

input = sys.stdin.readline

def func(row, col, size):
    dot = movie[row][col]

    for i in range(row, row + size):
        for j in range(col, col + size):
            if (dot != movie[i][j]):
                half = size // 2
                result.append("(")
                func(row, col, half)
                func(row, col + half, half)
                func(row + half, col, half)
                func(row + half, col + half, half)
                result.append(")")
                return

    result.append(dot)

n = int(input().rstrip('\n'))

movie = [list(map(int, input().rstrip('\n'))) for _ in range(n)]

result = []

func(0, 0, n)

print(''.join(map(str, result)))