import sys


def one_color(width_start, height_start, length):
    color = paper[width_start][height_start]
    for i in range(width_start, width_start + length):
        for j in range(height_start, height_start + length):
            if color != paper[i][j]:
                return False
    return True


def cut(width_start, height_start, length):
    # print("===================================")
    # for li in paper[width_start:width_start+length]:
    # print(li[height_start: height_start+length])
    if one_color(width_start, height_start, length):
        if paper[width_start][height_start] == WHITE:
            return (1, 0)
        else:
            return (0, 1)

    half = length // 2
    count = [0, 0]
    white_count, blue_count = cut(width_start, height_start, half)
    count[0] += white_count
    count[1] += blue_count

    white_count, blue_count = cut(width_start+half, height_start, half)
    count[0] += white_count
    count[1] += blue_count

    white_count, blue_count = cut(width_start, height_start+half, half)
    count[0] += white_count
    count[1] += blue_count

    white_count, blue_count = cut(width_start+half, height_start+half, half)
    count[0] += white_count
    count[1] += blue_count

    return count


input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

WHITE, BLUE = 0, 1
count = cut(0, 0, N)
for i in range(2):
    print(count[i])
