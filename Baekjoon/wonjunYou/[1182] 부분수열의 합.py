import sys

input = sys.stdin.readline

def func(total, cnt):
    global result
    if cnt == n:
        if total == s:
            result += 1
        return

    func(total + numbers[cnt], cnt + 1)
    func(total, cnt + 1)

n, s = map(int, input().rstrip('\n').split())
numbers = list(map(int, input().rstrip('\n').split()))

result = 0
func(0, 0)

if s == 0:
    print(result - 1)
else:
    print(result)