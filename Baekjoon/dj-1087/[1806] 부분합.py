import sys

input = sys.stdin.readline

N, S = map(int, input().split())
array = list(map(int, input().split()))

left, right = 0, 0
current_sum = array[0]
min_length = 100001
while (True):
    if (left > right) or (right >= len(array)):
        break

    if current_sum < S:
        right += 1
        if right >= len(array):
            break
        current_sum += array[right]
        continue

    # print("left, right", left, right)
    # print("array[left], array[right]", array[left], array[right])
    # print("length, min_length", right - left + 1, min_length)
    min_length = min(min_length, right - left + 1)
    current_sum -= array[left]
    left += 1

print(min_length if min_length != 100001 else 0)
