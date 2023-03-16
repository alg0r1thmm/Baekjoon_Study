import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]

#필요한 동전의 최소 개수를 저장
count = 0

#큰 가치 동전부터 필요한 동전 개수 계산
for coin in reversed(coins):
    count += k // coin
    k %= coin

print(count)
