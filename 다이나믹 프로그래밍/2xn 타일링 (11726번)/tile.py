# d[n] = d[n-1] + d[n-2]
import sys
INPUT = sys.stdin.readline

n = int(INPUT())  # n 입력받기
d = [0] * (n+1)  # DP 테이블 초기화
d[1] = 1  # n = 1일 때 초기값
if n > 1:
    d[2] = 2  # n = 2일 때 초기값

for i in range(3, n+1):  # i = 3부터 n까지 반복
    d[i] = (d[i-1] + d[i-2]) % 10007  # 점화식에 따라 DP 테이블 갱신

print(d[n])  # 결과 출력