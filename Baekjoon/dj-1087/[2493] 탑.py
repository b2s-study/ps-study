import sys


def find_reception_tower(reception_tower_stack, tower):
    while (True):
        if len(reception_tower_stack) == 0:
            break

        if reception_tower_stack[-1][1] > tower[1]:
            reception_tower_stack.append(tower)
            break

        reception_tower_stack.pop()

    return reception_tower_stack


input = sys.stdin.readline

N = int(input())
tower_list = list(enumerate(map(int, input().split())))

result_list = []
reception_tower_stack = []
for i in range(len(tower_list)):
    if i == 0:
        result_list.append(0)
        reception_tower_stack.append(tower_list[0])
        continue

    tower = tower_list[i]
    reception_tower_stack = find_reception_tower(reception_tower_stack, tower)
    if len(reception_tower_stack) == 0:
        result_list.append(0)
        reception_tower_stack.append(tower)
    else:
        reception_tower_number = reception_tower_stack[-2][0] + 1
        result_list.append(reception_tower_number)

print(" ".join(map(str, result_list)))
