import sys
input = sys.stdin.readline

N = int(input())
ans = 0
isused1 = [False for _ in range(40)] #같은 열에 있는지
isused2 = [False for _ in range(40)] # 좌측 하단 우측 상단 대각선
isused3 = [False for _ in range(40)] # 좌측 상단 우측 하단 대각선
def func(k):
    global ans
    if k == N:
        ans = ans +1
        return

    for i in range (N):
        if (isused1[i] or isused2[i + k] or isused3[k - i + N - 1] ):
            continue
        isused1[i] = True
        isused2[i + k] = True
        isused3[k - i + N -1] = True
        func(k + 1)
        isused1[i] = False
        isused2[i + k] = False
        isused3[k - i + N - 1] = False

func(0)
print(ans)
