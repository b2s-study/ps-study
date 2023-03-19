import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [0 for _ in range (10)]
temp = list(map(int,input().split()))
temp.sort()
def func(k):
    if k == m :
        for i in range(m):
            print(arr[i], end=' ')
        print()
        return
    remember = 0
    for temp_data in temp:
        if remember != temp_data and arr[k-1] <= temp_data:
            arr[k] = temp_data
            remember = temp_data
            func(k+1)

func(0)