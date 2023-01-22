import sys

input = sys.stdin.readline

n = int(input().rstrip('\n'))

distances = list(map(int, input().rstrip('\n').split()))
price = list(map(int, input().rstrip('\n').split()))

# 초기값 설정
move_distance = distances[0]
current_price = price[0]

result = 0

for idx in range(1, len(price) - 1):
    if current_price > price[idx]:
        result += move_distance * current_price
        move_distance = distances[idx]
        current_price = price[idx]
        continue

    move_distance += distances[idx]

result += move_distance * current_price

print(result)