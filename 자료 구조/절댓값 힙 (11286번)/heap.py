import heapq
import sys

n = int(sys.stdin.readline())
#우선순위 큐를 위한 heap 리스트 생성
heap = []

#주어진 값 n 만큼 반복
for _ in range(n):
    x = int(sys.stdin.readline())
    
    #입력된 값이 0인 경우 heap 비어있는지 확인
    #아닌 경우 가장 작은 값 출력
    if x == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(x), x))
