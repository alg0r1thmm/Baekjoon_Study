import sys

# 2차원 배열에서 (r,c)의 값을 찾는 함수
def z(n, r, c, x, y):
    # 종료 조건
    if n == 0:
        return 0
    
    # 현재 배열을 가로 세로로 반으로 나눈 중앙 값
    mid = 2**(n-1)
    
    # 4분면으로 나누어 처리
    if r < x + mid and c < y + mid: # 1사분면
        return z(n-1, r, c, x, y)
    elif r < x + mid and c >= y + mid: # 2사분면
        return mid*mid + z(n-1, r, c, x, y+mid)
    elif r >= x + mid and c < y + mid: # 3사분면
        return 2*mid*mid + z(n-1, r, c, x+mid, y)
    else: # 4사분면
        return 3*mid*mid + z(n-1, r, c, x+mid, y+mid)

# 입력 받기
N, r, c = map(int, sys.stdin.readline().split())

# 결과 출력
print(z(N, r, c, 0, 0))
