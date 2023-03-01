import sys


def get_k(N):
    temp = N//3
    k = 0
    while (True):
        if 2**k == temp:
            break
        k += 1
    return k


def generate(k):
    if k == 0:
        result = []
        result.append("  *  ")
        result.append(" * * ")
        result.append("*****")
        return result

    nk = k-1
    stars = generate(nk)
    result = []
    for prev in stars:
        side = " " * (3 * 2 ** nk)
        result.append(side + prev + side)

    for next in stars:
        result.append(next + " " + next)

    return result


input = sys.stdin.readline

N = int(input())
K = get_k(N)
stars = generate(K)
for s in stars:
    print(s)
