from collections import deque

n, k = map(int, input().split())

# 1부터 N까지의 숫자를 큐에 입력
queue = deque([i for i in range(1, n+1)])

# 결과를 저장할 리스트를 초기화
result = []

# 큐가 빌 때까지 반복
while queue:
    # K-1번째까지의 숫자를 왼쪽으로 회전시킵니다.
    for i in range(k-1):
        queue.append(queue.popleft())
    # K번째 숫자를 빼내서 결과 리스트에 추가
    result.append(str(queue.popleft()))

# 결과 리스트를 문자열로 변환하여 출력
print(f"<{', '.join(result)}>")


#입력값을 받아서 큐와 결과 리스트를 초기화
#큐에 1부터 N까지의 숫자 입력
#큐가 빌 때까지 다음을 반복
#큐에서 K-1번째까지의 숫자를 왼쪽으로 회전
#큐에서 K번째 숫자를 빼내서 결과 리스트에 추가
#결과 리스트를 문자열로 변환하여 출력