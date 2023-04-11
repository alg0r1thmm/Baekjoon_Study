from collections import deque

n, k = map(int, input().split())  # 위치 입력받기
MAX = 100001  # 최대 위치
visited = [False] * MAX  # 방문 여부 리스트 초기화
dist = [0] * MAX  # 거리 리스트 초기화

q = deque()  # 큐 생성
q.append(n)  # 시작점 큐에 삽입
visited[n] = True  # 시작점 방문 처리

while q:  # BFS 알고리즘 수행
    x = q.popleft()
    if x == k:  # 동생 위치에 도달하면 거리 출력 후 종료
        print(dist[x])
        break

    # x-1 위치 방문 처리
    if x-1 >= 0 and not visited[x-1]:
        q.append(x-1)
        visited[x-1] = True
        dist[x-1] = dist[x] + 1

    # x+1 위치 방문 처리
    if x+1 < MAX and not visited[x+1]:
        q.append(x+1)
        visited[x+1] = True
        dist[x+1] = dist[x] + 1

    # 2*x 위치 방문 처리
    if 2*x < MAX and not visited[2*x]:
        q.append(2*x)
        visited[2*x] = True
        dist[2*x] = dist[x] + 1