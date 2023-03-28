import sys

N = int(sys.stdin.readline())  # 입력받을 종이의 크기
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 각 좌표에 쓰인 숫자를 저장하는 리스트

result = []  # 정답을 저장할 리스트

# 종이를 나누는 재귀함수
def solution(x, y, N) :
  color = paper[x][y]  # 해당 영역의 색깔을 저장
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != paper[i][j] :  # 해당 영역의 색깔이 다르면, 4개의 작은 종이로 나눔
        solution(x, y, N//2)
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return
  if color == 0 :  # 해당 영역이 전부 0이면 result 리스트에 0 추가
    result.append(0)
  else :  # 해당 영역이 전부 1이면 result 리스트에 1 추가
    result.append(1)

# 정사각형 종이 전체에 대해 solution 함수 실행
solution(0,0,N)
# 결과 출력
print(result.count(0))
print(result.count(1))
