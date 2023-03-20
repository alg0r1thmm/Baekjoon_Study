n = int(input())
m = int(input())
K = [[] for _ in range(n+1)]
L = [False] * (n+1)

# 인접 리스트 생성
for _ in range(m):
    a, b = map(int, input().split())
    K[a].append(b)
    K[b].append(a)

def DFS(v):
    L[v] = True
    for i in K[v]:
        if not L[i]:
            DFS(i)

DFS(1)
print(L.count(True)-1)
