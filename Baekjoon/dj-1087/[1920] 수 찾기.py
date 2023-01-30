# 이슈사항
# - 이분탐색으로 시간초과 뜸

import sys


def binary_search2(num, arr):
    # 재귀로 풀 경우 시간 초과. why?
    if len(arr) == 0:
        return "0"

    mid_idx = len(arr) // 2
    if num < arr[mid_idx]:
        return binary_search(num, arr[:mid_idx])
    elif arr[mid_idx] < num:
        return binary_search(num, arr[mid_idx+1:])
    else:
        return "1"


def binary_search(num, arr):
    # while로 풀어도 시간 초과? why??
    start = 0
    end = len(arr)
    while (True):
        if len(arr[start:end]) == 0:
            break

        mid = (start + end) // 2
        if num < arr[mid]:
            end = mid
        elif num > arr[mid]:
            start = mid + 1
        else:
            return "1"

    return "0"


input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
A = list(map(int, input().split()))
# A = set(map(int, input().split()))
M = int(input())
to_find = list(map(int, input().split()))

A.sort()
for num in to_find:
    result = binary_search(num, A)
    print(result + "\n")

# for num in to_find:
#     if num in A:
#         print("1\n")
#     else:
#         print("0\n")
