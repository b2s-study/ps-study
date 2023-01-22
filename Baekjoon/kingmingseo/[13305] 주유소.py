import sys
input= sys.stdin.readline

city=int(input())
dist=list(map(int,input().split()))
price=list(map(int,input().split()))
total=dist[0]*price[0]
min_price=price[0]
j=0
for i in range (1,city-1):
    if min_price>price[i]:
        min_price=price[i]

    total=total+min_price*dist[i]

print(total)

