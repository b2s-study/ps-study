import sys


def binary_search(num, arr):
    start = 0
    end = len(arr) - 1
    while (True):
        if start > end:
            break

        mid = (start + end) // 2
        if num < arr[mid]:
            end = mid - 1

        elif num > arr[mid]:
            start = mid + 1

        else:
            return 1

    return 0


input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
# A = set(map(int, input().split()))
M = int(input())
search_list = list(map(int, input().split()))

A.sort()
for num in search_list:
    result = binary_search(num, A)
    print(result)

# for num in search_list:
#     if num in A:
#         print(1)
#     else:
#         print(0)
