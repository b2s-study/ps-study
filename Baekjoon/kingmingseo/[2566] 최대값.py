import sys
input= sys.stdin.readline

array = []
max=-99999

for i in range(9):
    array.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        if (array[i][j]>max):
            max=array[i][j]
            col=i+1
            row=j+1
print(max)
print(col,row)