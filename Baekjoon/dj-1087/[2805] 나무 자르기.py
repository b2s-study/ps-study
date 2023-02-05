import sys

# 핵심 로직 - 나무 높이를 이분 탐색
# 탐색 범위: 0~최대 나무 높이

input = sys.stdin.readline

N, M = map(int, input().split())
tree_list = list(map(int, input().split()))

min_height, max_height = 0, max(tree_list)
while (True):
    mid_height = (min_height + max_height) // 2
    if min_height > max_height:
        break

    get_tree_length = 0
    for height in tree_list:
        if height <= mid_height:
            continue
        get_tree_length += height - mid_height

    if get_tree_length < M:
        max_height = mid_height - 1
    elif get_tree_length > M:
        min_height = mid_height + 1
    else:
        break

print(mid_height)
