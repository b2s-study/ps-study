import sys
input = sys.stdin.readline
temp=input().rstrip()
temp2=temp.upper()

bin=[]
bin2=set()
button=False
max=-1
alphabet=""

for i in range(0,len(temp2)):
    bin.append(temp2[i])
    bin2.add(temp2[i])

for i in bin2:

    if(bin.count(i)>max):
        alphabet=i
        max=bin.count(i)
        button=False

    elif(bin.count(i)==max):
        button=True


if(button==True):
    print("?")

else:
    print(alphabet)









