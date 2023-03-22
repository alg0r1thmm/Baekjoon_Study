import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

# DFS 함수
def dfs(x, y):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
            dfs(nx, ny)

t = int(input().rstrip())

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                
                dfs(i, j)
                cnt += 1
                
    print(cnt)
