from collections import deque
import sys

# 입력 받기
m, n = map(int, sys.stdin.readline().split())
tomato_box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# BFS 알고리즘을 이용하여 최소 일수 계산하기
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()

for i in range(n):
    for j in range(m):
        if tomato_box[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and tomato_box[nx][ny] == 0:
            tomato_box[nx][ny] = tomato_box[x][y] + 1
            queue.append((nx, ny))

# 결과 출력하기
max_day = 0
for row in tomato_box:
    if 0 in row:
        print("-1")
        exit()
    max_day = max(max_day, max(row))

print(max_day - 1)
