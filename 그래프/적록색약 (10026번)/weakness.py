import sys

INPUT = sys.stdin.readline

# 재귀함수 호출 제한을 늘려줌 (기본값: 1000)
sys.setrecursionlimit(100000)

# 그리드의 크기 입력
n = int(INPUT())

# 그리드 생성
graph = [list(INPUT()) for _ in range(n)]

# 방문 여부 체크 리스트 생성
visited = [[False]*n for _ in range(n)]

# 상하좌우 이동을 위한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 깊이 우선 탐색 함수
def dfs(x, y, color_blindness):
    visited[x][y] = True
    # 상하좌우 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 그리드를 벗어나면 continue
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        # 이미 방문한 곳이면 continue
        if visited[nx][ny]:
            continue
        # 적록색약일 때
        if color_blindness:
            # 빨강, 초록은 같은 구역으로 처리
            if graph[x][y] == 'R' or graph[x][y] == 'G':
                if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                    dfs(nx, ny, True)
            # 파랑은 그대로 처리
            else:
                if graph[x][y] == graph[nx][ny]:
                    dfs(nx, ny, True)
        # 적록색약이 아닐 때
        else:
            # 색이 같으면 같은 구역으로 처리
            if graph[x][y] == graph[nx][ny]:
                dfs(nx, ny, False)

# 적록색약이 아닌 사람이 보는 구역의 수 구하기
count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, False)
            count += 1

# 결과 출력 (적록색약이 아닌 경우의 구역 수)
print(count, end=' ')

# 방문 여부 체크 리스트 초기화
visited = [[False]*n for _ in range(n)]

# 적록색약인 사람이 보는 구역의 수 구하기
count = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, True)
            count += 1

# 결과 출력 (적록색약인 경우의 구역 수)
print(count)
