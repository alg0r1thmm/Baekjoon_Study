from collections import deque

N = int(input())

#카드에 대한 리스트 생성
cards = deque(range(1, N+1))

#카드가 하나 남을 때 까지 반복
while len(cards) > 1:
    #맨 앞에 있는 값 버리기
    cards.popleft()
    #다음 카드 맨 뒤로 이동
    cards.rotate(-1)

#최종 값 출력
print(cards[0])