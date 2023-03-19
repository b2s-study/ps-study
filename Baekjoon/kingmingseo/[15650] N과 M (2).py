import sys
input = sys.stdin.readline

n , m = map(int,input().split())

arr = [0 for _ in range (10)]
isused = [False for _ in range (10)]

def func(k):
    if k == m :
        for i in range (0,m):
            print(arr[i], end=' ')
        print()
        return

    for i in range(1,n+1):
        if isused[i] == False and arr[k-1] < i :
            arr[k] = i
            isused[i] = True
            func(k+1)
            isused[i] = False

func(0)
