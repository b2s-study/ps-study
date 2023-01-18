import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    importance_list = list(map(int, input().split()))
    target_cache = [0] * N
    target_cache[M] = 1
    order = 1
    while (True):
        if importance_list[0] == max(importance_list):
            if target_cache[0] == 1:
                break

            order += 1
            del importance_list[0]
            del target_cache[0]
            continue

        importance = importance_list[0]
        importance_list.append(importance)
        del importance_list[0]

        target = target_cache[0]
        target_cache.append(target)
        del target_cache[0]

    print(order)
