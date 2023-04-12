import sys

INPUT = sys.stdin.readline

sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 높여주기

n, m = map(int, INPUT().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, INPUT().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)  # 방문 여부를 체크할 리스트

def dfs(x):
    visited[x] = True  # 방문한 정점 체크
    for y in graph[x]:  # 현재 정점에 연결된 정점들 중
        if not visited[y]:  # 아직 방문하지 않은 정점이 있는 경우
            dfs(y)  # 해당 정점을 시작점으로 다시 DFS 수행

cnt = 0  # 연결 요소의 개수
for i in range(1, n + 1):
    if not visited[i]:  # 방문하지 않은 정점이라면
        dfs(i)  # DFS 수행
        cnt += 1  # DFS 수행이 끝나면 연결 요소 개수 1 증가

print(cnt)
