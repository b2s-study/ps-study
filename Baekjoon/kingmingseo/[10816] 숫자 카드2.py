import sys
input = sys.stdin.readline

data_num = int(input())
data = list(map(int,input().split()))
check_num = int(input())
check_list = list(map(int,input().split()))
dic = {}

for temp in data:
    dic[temp]=0
for temp in data:
    dic[temp]=dic[temp]+1

for check_data in check_list:
    if check_data in dic:
        print(dic[check_data], end=' ')
    else:
        print(0,end=' ')


