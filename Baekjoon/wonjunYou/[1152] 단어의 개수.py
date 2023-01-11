import sys

input = sys.stdin.readline

result = 0
result_pos = [1, 1]

for row in range(9):
    numbers = list(map(int, input().rstrip('\n').split()))

    for col in range(9):
        if numbers[col] > result:
            result = numbers[col]
            result_pos[0], result_pos[1] = row + 1, col + 1

print(result)
print(*result_pos)