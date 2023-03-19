import sys
input = sys.stdin.readline

n, m = map(int,input().split())
data = list(map(int,input().split()))
isused = [False for _ in range (10001)]
arr = [0 for _ in range(10)]
data.sort()
def func(k):
    if k == m:
        for i in range(m):
            print(arr[i],end = ' ')
        print()
        return

    for temp_data in data:
        if isused[temp_data] == False and arr[k-1] < temp_data :
            arr[k] = temp_data
            isused[temp_data] == True
            func(k+1)
            isused[temp_data] == False

func(0)