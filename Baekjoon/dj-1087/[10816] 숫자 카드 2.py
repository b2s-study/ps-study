import sys

# ======================= init ======================= #
input = sys.stdin.readline

N = int(input())
card_list = list(map(int, input().split()))
M = int(input())
search_list = list(map(int, input().split()))


# ======================= solve1 ======================= #
# 방안 1) 바킹독 풀이 [실패]
# 핵심 로직 - 이분 탐색
'''
사전 작업: 배열 정렬 (오름차순)
ex> [2, 4, 6, 10, 10, 16, 16, 16, 30, 32]

if count 16 <- 존재하는 값일 경우
1. first 16 index: 5
2. last 16 index: 7
3. result: 7 - 5 + 1 = 3

if count 12 <- 존재하지 않는 값일 경우
1. first 12 index: return -1
2. last 12 index: return -1
3. result: (-1) - (-1) = 0 
'''


def search_first_index(array, value):
    start, end = 0, len(array) - 1
    while (True):
        if start > end:
            break
        elif (start == end) and (array[start] == value):
            return start

        mid = (start + end) // 2
        if value <= array[mid]:
            # mid 값은 내림값이기 때문에 점진적으로 내려갈 수 밖에 없음
            end = mid
        else:
            start = mid + 1

    return -1


def search_last_index(array, value):
    start, end = 0, len(array) - 1
    while (True):
        if start > end:
            break
        elif (start == end) and (array[end] == value):
            return end

        mid = (start + end) // 2 + 1
        if value >= array[mid]:
            # mid 값을 올림값으로 설정해야 점진적으로 올라가게 됨!!
            start = mid + 1
        else:
            end = mid - 1

    return start

# card_list.sort()
# result = []
# for value in search_list:
#     first_idx = search_first_index(card_list, value)
#     last_idx = search_last_index(card_list, value)
#     print("first_idx, last_idx >>", first_idx, last_idx)
#     count = last_idx - first_idx + 1
#     result.append(count)
# print(*result)


# ======================= solve2 ======================= #
# 방안 2) 해쉬 맵 (성공)
# 핵심 로직 - count dictionary
'''
ex> [2, 4, 6, 10, 10, 16, 16, 16, 30, 32]

count_dict = {2:1, 4:1, 6:1, 10:2, 16:3, 30:1, 32:1}

- 16을 찾을 경우:
if count_dict.get(16): 
    print(count_dict[16])
else: 
    print(0)

dictionary에 없는 key일 경우 get()은 None을 return 함
'''

count_dict = {}
for card in card_list:
    if count_dict.get(card):
        count_dict[card] += 1
    else:
        count_dict[card] = 1

for target in search_list:
    result = count_dict.get(target)
    if result:
        print(result, end=" ")
    else:
        print(0, end=" ")
