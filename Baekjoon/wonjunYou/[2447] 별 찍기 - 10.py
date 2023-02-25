import sys

sys.setrecursionlimit(10**4)
def draw_star(n):

	global Map
	if n == 3:
		for i in range(3):
			for j in range(3):
				Map[0][:3] = Map[2][:3] = [1] * 3
				Map[1][:3] = [1, 0, 1]
		return
	a = n//3
	draw_star(a)

	for i in range(3):
		for j in range(3):
			if i == 1 and j == 1:
				continue
			else:
				for k in range(a):
					Map[a*i + k][a*j : a*(j+1)] = Map[k][:a]

n = int(sys.stdin.readline().rstrip('\n'))
Map = [[0 for _ in range(n)] for _ in range(n)]

draw_star(n)

for i in Map:
	for j in i:
		if j:
			print('*', end="")
		else:
			print(' ', end="")

	print()