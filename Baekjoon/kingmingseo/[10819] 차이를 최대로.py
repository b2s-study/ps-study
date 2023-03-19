import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int,input().split()))
isused = [False for _ in range(N)]
answer = 0
def func(k):
    global answer

    if len(k) == N:
        total = 0
        for i in range(N-1):
            total = total + abs(k[i] - k [i+1])
        answer = max(total, answer)
        return


    for i in range(N):
        if isused[i] == False:
            isused[i] = True
            k.append(data[i])
            func(k)
            isused[i] = False
            k.pop()

func([])
print(answer)
