
import sys

input = sys.stdin.readline

k = int(input())

st = []
for _ in range(k):
    num = int(input())
    if num==0:
        st.pop()
        continue
    st.append(num)

print(sum(st))