import sys

N = int(sys.stdin.readline())

# dp1: dp1(n)의 값을 저장할 변수, 초기값 1
# dp2: dp1(n-1)의 값을 저장할 변수, 초기값 0
dp1, dp2 = 1, 0

# 피보나치 수열 계산
for i in range(N):
    dp1, dp2 = (dp1+dp2)%10, dp1%10

# 결과 출력
print(dp1)
