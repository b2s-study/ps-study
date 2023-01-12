import math
import sys
input=sys.stdin.readline
test=int(input())

dist=[]
for i in range(test):
    x,y=map(int,input().split())
    dist.append(y-x)


for i in dist:

    temp=math.floor(i ** (1 / 2))

    if i==1 :
        print(1)
    elif i==2:
        print(2)
    elif i==3:
        print(3)

    elif (temp**2==i):
        print(temp*2-1)
    elif (temp ** 2 + temp < i):
        print(temp* 2 + 1)

    elif(temp**2<i):
        print(temp*2)








