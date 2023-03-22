import sys

def TSP(now, cnt):
    if dp[now][cnt]:
        return dp[now][cnt]

    # 모든 도시를 방문한 경우
    if cnt == all_visited:
        return path[now][0] if path[now][0] > 0 else float('inf')

    cost = float('inf')
    # 모든 도시 순회
    for i in range(n):
        # 현재 위치와 같은 도시가 아니고, 아직 방문하지 않은 도시일 경우
        # 그리고 현재 위치에서 해당 도시로 이동이 가능한 경우
        if i != now and not cnt & (1 << i) and path[now][i] > 0:
            # 해당 도시 방문
            val = TSP(i, cnt | (1 << i))
            # 최소 비용 갱신
            cost = min(cost, val + path[now][i])

    # dp 테이블에 값 저장
    dp[now][cnt] = cost
    return dp[now][cnt]

n = int(sys.stdin.readline())
path = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * (1 << n) for _ in range(n)]
all_visited = (1 << n) - 1

print(TSP(0, 1))
