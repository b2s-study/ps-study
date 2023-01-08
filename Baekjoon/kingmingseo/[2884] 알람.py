import sys
input=sys.stdin.readline

hour, minute =map(int,input().split())
minute=minute-45

if (minute<0):
    hour=hour-1
    minute=60+minute
    

if(hour<0):
    hour=24-1

print(hour, minute)
