import sys

n, k = map(int, sys.stdin.readline().split())

# 파스칼의 삼각형을 저장할 이차원 리스트 초기화
triangle = [[1] * i for i in range(1, n+1)]

# 파스칼의 삼각형을 채우는 반복문
for i in range(2, n):
    for j in range(1, i):
        triangle[i][j] = triangle[i-1][j-2] + triangle[i-1][j]

print(triangle[n-1][k-1])
