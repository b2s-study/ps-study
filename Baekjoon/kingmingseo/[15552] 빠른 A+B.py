import sys
input=sys.stdin.readline

n=int(input())
temp=[]
for i in range(1,n+1):
    a , b = map(int, input().split())
    temp.append(a+b)

for i in temp:
    print(i)

