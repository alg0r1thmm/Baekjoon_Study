import heapq
import sys

heap = []

# 입력받은 명령의 개수를 저장
n = int(sys.stdin.readline())

# 입력받은 명령을 하나씩 처리
for i in range(n):
    x = int(sys.stdin.readline())
    
    # 입력받은 수가 0인 경우, 힙에서 가장 작은 수를 출력하고 그 수를 삭제
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    # 입력받은 수가 0이 아닌 경우, 힙에 해당 수를 추가
    else:
        heapq.heappush(heap, x)
