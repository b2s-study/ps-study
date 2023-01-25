import sys
input= sys.stdin.readline
grade=[]
person=int(input())
array = [[0 for i in range(2)] for i in range(person)]

for i in range (person):
    array[i]=list(map(int,input().split()))

for i in range (person):
    now_weight=array[i][0]
    now_height=array[i][1]
    now_grade=1
    for j in range (person):
        if(now_weight<array[j][0] and now_height<array[j][1] ):
            now_grade=now_grade+1


    grade.append(now_grade)


for i in range(person):
    print(grade[i],end=" ")
