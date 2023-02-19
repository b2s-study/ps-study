import sys


def can_zip(si, sj, length):
    # binary_number
    bn = video[si][sj]
    for i in range(si, si + length):
        for j in range(sj, sj + length):
            if video[i][j] != bn:
                return False
    return True


def divide(si, sj, length):
    if can_zip(si, sj, length):
        bn = video[si][sj]
        return str(bn)

    half = length // 2
    result = '('
    result += divide(si, sj, half)
    result += divide(si, sj + half, half)
    result += divide(si + half, sj, half)
    result += divide(si + half, sj + half, half)
    result += ')'
    return result


input = sys.stdin.readline

N = int(input())
video = [list(map(int, list(input().rstrip()))) for _ in range(N)]
zip_code = divide(0, 0, N)
print(zip_code)
