import sys
input = sys.stdin.readline

n , m = map(int,input().split())
arr = [0 for _ in range (10)]
def func (k):
    if k == m :
        for i in range (m):
            print(arr[i], end = ' ')
        print()
        return

    for i in range(1,n+1):
        if arr[k-1] <= i :
            arr[k] = i
            func(k+1)

func(0)