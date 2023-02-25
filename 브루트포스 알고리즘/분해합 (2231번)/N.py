#분해합 반환하는 함수
def get_M(N):
    return N + sum(map(int, str(N)))

#처음 입력받는 값인 N 입력
N = int(input())

#구해야하는 값인 M값 0으로 초기화
M = 0

#1부터 N까지 수 생성하는 반복문
for i in range(1, N+1):
    #지속적으로 리스트 순회하며 분해합 선정
    #분해합이 N과 같은 경우 해당 수 return
    if get_M(i) == N:
        M = i
        break

print(M)