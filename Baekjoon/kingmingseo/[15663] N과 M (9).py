import sys
import copy
input = sys.stdin.readline

n, m = map(int,input().split())
temp = list(map(int,input().split()))
arr = [0 for _ in range(10)]
isused = [False for _ in range (10001)]
temp.sort()
data = {}
for i in temp:
    data[i] = 0

for i in temp:
    data[i] = data[i] + 1


def func(k):
    if k == m :
        for i in range(m):
            print(arr[i], end = ' ')
        print()
        return

    remember = 0
    for temp_data in temp:
       if isused[temp_data] == False and remember != temp_data :
            arr[k] = temp_data
            data[temp_data] = data[temp_data] - 1
            if data[temp_data] == 0:
                isused[temp_data] = True
            remember = temp_data
            func(k+1)
            isused[temp_data] = False
            data[temp_data] = data[temp_data] + 1

func(0)
