import sys 
input= sys.stdin.readline


temp=set()

for i in range(10):
    a=int(input())
    temp.add(a%42)

print(len(temp))