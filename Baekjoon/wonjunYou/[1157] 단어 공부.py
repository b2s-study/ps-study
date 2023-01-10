import sys

input = sys.stdin.readline

word = input().rstrip('\n').upper()

alphas = list(set(word))

alpha_counter = []

for alpha in alphas:
    alpha_counter.append(word.count(alpha))

if alpha_counter.count(max(alpha_counter)) > 1:
    print("?")

else:
    print(alphas[alpha_counter.index(max(alpha_counter))])