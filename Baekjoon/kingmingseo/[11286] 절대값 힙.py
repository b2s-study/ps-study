from queue import PriorityQueue
import sys

input = sys.stdin.readline
count = int(input())
q = PriorityQueue()
temp = []

for k in range(count):
    a = int(input())
    temp.append(a)

for i in temp:
    if i > 0:
        q.put((i, '+'))

    elif q.qsize() == 0 and i == 0:
        print(0)

    elif i == 0:
        value = q.get()
        if value[1] == '-':
            print(int((value[0] * -1)-0.5 ))
        else:
            print(value[0])

    elif i < 0:
        q.put((-1 * i -0.5 , '-'))