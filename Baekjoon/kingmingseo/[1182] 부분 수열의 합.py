import sys
input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0

def func(idx,sub_sum):
    global answer
    if idx == n :
        return

    sub_sum = sub_sum + arr[idx]

    if sub_sum == s :
        answer = answer +1

    func(idx + 1 , sub_sum)
    func(idx +1 , sub_sum - arr[idx])

func(0,0)
print(answer)


