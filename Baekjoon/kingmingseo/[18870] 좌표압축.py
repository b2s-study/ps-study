import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
data_set =set(data)
data_list =list(data_set)

data_list.sort()


coordinate = {}
i=0

for check_data in data_list:
    coordinate[check_data] = i
    i = i +1

for temp in data:
    print(coordinate[temp], end = ' ')