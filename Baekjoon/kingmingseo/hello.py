import sys
input=sys.stdin.readline

num1=int(input())
card=list(map(int,input().split()))

num2=int(input())
check=list(map(int,input().split()))

card.sort()
def binary_search(array,target,start,end):
    while (start<=end):
        mid=(start+end)//2

        if (array[mid]==target):
            return 1
        elif (array[mid]<target):
            start=mid+1
        elif (array[mid]>target):
            end=mid-1
        else:
            return None


for i in range(num2):
    if binary_search(card,check[i],0,num1-1) != None:
        print(1,end=" ")
    else:
        print(0,end=" ")