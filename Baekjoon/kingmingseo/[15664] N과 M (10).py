import sys
input = sys.stdin.readline

n, m = map(int,input().split())
temp = list(map(int,input().split()))
temp.sort()
data = {}
arr = [0 for _ in range (10)]
isused = [False for _ in range (10001)]

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
        if arr[k-1] <= temp_data and remember != temp_data and isused[temp_data] == False :
            arr[k] = temp_data
            data[temp_data] = data[temp_data] - 1
            remember = temp_data
            if data[temp_data] == 0 :
                isused[temp_data] = True
            func(k+1)
            isused[temp_data] = False
            data[temp_data] = data[temp_data] + 1
func(0)