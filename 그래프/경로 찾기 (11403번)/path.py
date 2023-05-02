import sys

INPUT = sys.stdin.readline

# DFS
def dfs(v, path, node, n):
    for i in range(n):
        # 인접하면서 방문하지 않은 값 탐색
        if path[v][i] == 1 and not node[i]:
            node[i] = 1
            dfs(i, path, node, n)

n = int(INPUT())
path = [list(map(int, INPUT().split())) for _ in range(n)]

# 정점 이동 하는 경우에 초기화
result = [[0] * n for _ in range(n)]

# 모든 정점에 대한 DFS 적용
for i in range(n):
    node = [0] * n
    dfs(i, path, node, n)

    # 정점 이동 여부에 따른 행렬 저장
    for j in range(n):
        result[i][j] = node[j]

for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print()