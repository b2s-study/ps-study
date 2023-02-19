import sys


def generate(N):
    if N == 1:
        result = ["*"]
        return result

    stars = generate(N//3)
    result = []
    for s in stars:
        result.append(s*3)
    for s in stars:
        result.append(s + " "*(N//3) + s)
    for s in stars:
        result.append(s*3)

    return result


input = sys.stdin.readline

N = int(input())

stars = generate(N)
print('\n'.join(stars))
