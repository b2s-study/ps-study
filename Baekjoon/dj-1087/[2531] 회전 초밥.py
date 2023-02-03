import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
rotation_sushi = [int(input()) for _ in range(N)]

sushi_list = rotation_sushi + rotation_sushi[0: k]
current_kinds = 0
count_list = [0] * (d+1)
for i in range(k):
    sushi = sushi_list[i]
    if count_list[sushi] == 0:
        current_kinds += 1
    count_list[sushi] += 1
if count_list[c] == 0:
    current_kinds += 1
count_list[c] += 1


start = 0
max_kinds = current_kinds
while (True):
    # print("current_sushi_list >>", sushi_list[start:start+k])
    # print("current_kinds >>", current_kinds)

    if start + k >= len(sushi_list):
        break

    first_sushi = sushi_list[start]
    count_list[first_sushi] -= 1
    if count_list[first_sushi] == 0:
        current_kinds -= 1

    last_sushi = sushi_list[start+k]
    if count_list[last_sushi] == 0:
        current_kinds += 1
    count_list[last_sushi] += 1

    max_kinds = max(max_kinds, current_kinds)
    start += 1

print(max_kinds)
