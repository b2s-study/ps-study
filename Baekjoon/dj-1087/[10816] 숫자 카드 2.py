# 이슈사항
# - 구지 이분탐색을 쓸 이유가 있을까?
# - 쓴다면 어떻게?

import sys

input = sys.stdin.readline

N = int(input())
card_list = list(map(int, input().split()))
M = int(input())
search_list = list(map(int, input().split()))

card_dict = {}
for card in card_list:
    if card_dict.get(card):
        card_dict[card] += 1
    else:
        card_dict[card] = 1

for target in search_list:
    result = card_dict.get(target)
    if result:
        print(result, end=" ")
    else:
        print(0, end=" ")
