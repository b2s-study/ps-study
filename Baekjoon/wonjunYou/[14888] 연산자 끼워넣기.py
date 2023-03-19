import sys

input = sys.stdin.readline

def dfs(depth, plus, minus, multiply, divide, total):
    global max_result, min_result

    if depth == n:
        max_result = max(max_result, total)
        min_result = min(min_result, total)
        return

    if plus:
        dfs(depth + 1, plus - 1, minus, multiply, divide, total + numbers[depth])

    if minus: 
        dfs(depth + 1 , plus, minus - 1, multiply, divide, total - numbers[depth])

    if multiply:
        dfs(depth + 1 , plus, minus, multiply - 1, divide, total * numbers[depth])

    if divide:
        dfs(depth + 1 , plus, minus, multiply, divide - 1, int(total / numbers[depth]))

n = int(input().rstrip('\n'))
numbers = list(map(int, input().rstrip('\n').split()))
operators = list(map(int, input().rstrip('\n').split()))

max_result = float("-inf")
min_result = float("inf")

dfs(1, operators[0], operators[1], operators[2], operators[3], numbers[0])
print(max_result)
print(min_result)