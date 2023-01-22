import sys

input = sys.stdin.readline

brackets = list(input().rstrip('\n'))

cnt = 0
result = 0

idx = 0

while (idx < len(brackets)):
    if (idx == len(brackets) - 1):
        result += 1
        break

    if brackets[idx] == "(":
        # 1. 레이저 발사
        if brackets[idx + 1] == ")":
            result += cnt
            idx += 2
            continue

        # 2. 열린 괄호를 만나는 경우 : 막대기가 하나 추가된다.
        else:
            cnt += 1

    # 3. 닫힌 괄호를 만나는 경우 : 막대기의 끝을 의미
    else:
        result += 1
        cnt -= 1

    idx += 1

print(result)
