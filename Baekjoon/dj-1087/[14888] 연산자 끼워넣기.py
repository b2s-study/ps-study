import sys


def calculate(a, b, operator):
    global PLUS, MINUS, MULTIPLY, DIVIDE
    if operator == PLUS:
        return a+b
    if operator == MINUS:
        return a-b
    if operator == MULTIPLY:
        return a*b
    if operator == DIVIDE:
        if a < 0:
            return -1 * ((-1 * a) // b)
        return a // b


def dfs(num_idx, val):
    global numbers, operators, used, min_val, max_val
    if num_idx == len(numbers):
        min_val = min(min_val, val)
        max_val = max(max_val, val)
        return val

    number = numbers[num_idx]
    for idx in range(len(operators)):
        if not used[idx]:
            used[idx] = True
            new_val = calculate(val, number, operators[idx])

            dfs(num_idx+1, new_val)

            used[idx] = False


input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
# [+, -, *, //], 나눗셈의 경우, 양수 치환 후 몫을 음수로 치환
operator_counts = list(map(int, input().split()))

# dfs로 숫자 하나 하나 씩 연산해 나간다
# 모든 숫자를 연산 후 값을 리턴
# 리턴 받은 값으로 최댓값, 최솟값 업데이트

used = [False] * (N-1)
PLUS, MINUS, MULTIPLY, DIVIDE = 0, 1, 2, 3
operators = []
for operator, count in list(enumerate(operator_counts)):
    operators.extend([operator] * count)

min_val = sys.maxsize
max_val = -1 * sys.maxsize
dfs(1, numbers[0])
print(max_val)
print(min_val)
