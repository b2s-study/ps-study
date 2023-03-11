import sys


def is_valid(password):
    vowel_counts = 0      # 모음 개수
    consonant_counts = 0  # 자음 개수
    for c in password:
        if c in vowels:
            vowel_counts += 1
        else:
            consonant_counts += 1
    return vowel_counts >= 1 and consonant_counts >= 2


def dfs(idx=-1):
    global password, L, C, alphabet
    if len(password) == L:
        if is_valid(password):
            print("".join(password))
        return

    for i in range(idx+1, C):
        password.append(alphabet[i])
        dfs(i)
        password.pop()


# 제약조건: 모음 1개이상, 자음 2개이상
input = sys.stdin.readline

L, C = map(int, input().split())
alphabet = input().rstrip().split()
alphabet.sort()

vowels = set(["a", "e", "i", "o", "u"])
password = []
dfs()
