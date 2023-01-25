import sys
input = sys.stdin.readline
n = int(input())
n2= input()
temp=[]
sum=0

for i in range (n):
    temp.append(int(n2[i]))


for i in temp:
    sum=sum+i

print(sum)

