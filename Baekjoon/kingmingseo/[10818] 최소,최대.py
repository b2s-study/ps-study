import sys
input=sys.stdin.readline

n=int(input())
temp=[0 for i in range(n)]
temp=list(map(int,input().split()))

temp.sort()
print(temp[0],end="")

temp.sort(reverse=True)
print("",temp[0])

