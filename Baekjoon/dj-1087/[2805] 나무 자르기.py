import sys

input = sys.stdin.readline

N, M = map(int, input().split())
tree_list = list(map(int, input().split()))

min_height, max_height = 0, max(tree_list)
H = (min_height + max_height) // 2
while(min_height <= max_height):
    H = (min_height + max_height) // 2
    get_length = 0
    for each in tree_list:
        get_length += max(each - H, 0)

    if get_length < M:
        max_height = H - 1
    elif get_length > M:
        min_height = H + 1
    else:
        break

print(H)
