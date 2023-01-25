import sys
input=sys.stdin.readline

temp=input().rstrip()
sum=0
temp2=set()


for i in range (1,len(temp)+1):
    j = 0
    while (j+i<=len(temp)):
        temp2.add(temp[j:j+i])
        j=j+1



print (len(temp2))