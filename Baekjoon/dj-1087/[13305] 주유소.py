import sys

input = sys.stdin.readline

N = int(input())
distance_list = list(map(int, input().split()))
oil_price_list = list(map(int, input().split()))

total_price = 0
current_oil_price = oil_price_list[0]
for i in range(N-1):
  distance = distance_list[i]
  total_price += current_oil_price * distance

  next_oil_price = oil_price_list[i+1]
  if current_oil_price > next_oil_price:
    current_oil_price = oil_price_list[i+1]

print(total_price)