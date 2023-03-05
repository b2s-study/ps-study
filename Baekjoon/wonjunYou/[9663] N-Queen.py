import sys

input = sys.stdin.readline


def func(cur):
    global cnt

    if (cur == n):
        cnt += 1
        return

    for i in range(0, n):
        # check
        if isused1[i] or isused2[i + cur] or isused3[cur - i + n - 1]:
            continue

        isused1[i] = 1
        isused2[i + cur] = 1
        isused3[cur - i + n - 1] = 1

        func(cur + 1)

        isused1[i] = 0
        isused2[i + cur] = 0
        isused3[cur - i + n - 1] = 0


n = int(input().rstrip('\n'))

cnt = 0
isused1 = [0 for _ in range(n)]
isused2 = [0 for _ in range(2 * n)]
isused3 = [0 for _ in range(2 * n)]

func(0)

print(cnt)