import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))
arr = [0 for _ in range(10)]
data.sort()


def func(k):
    if k == m:
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return

    for temp_data in data:
        arr[k] = temp_data
        func(k + 1)


func(0)