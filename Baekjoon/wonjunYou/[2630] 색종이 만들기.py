import sys

input = sys.stdin.readline

def cut_paper(row, col, size):
    global white, blue
    color = paper[row][col]

    for i in range(row, row + size):
        for j in range(col, col + size):
            if (paper[i][j] != color):
                half = size // 2

                cut_paper(row, col, half)
                cut_paper(row, col + half, half)
                cut_paper(row + half, col, half)
                cut_paper(row + half, col + half, half)
                return

    if paper[row][col] == 1:
        blue += 1

    elif paper[row][col] == 0:
        white += 1

n = int(input().rstrip('\n'))

paper = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]

white = 0
blue = 0

cut_paper(0, 0, n)

print(white)
print(blue)
