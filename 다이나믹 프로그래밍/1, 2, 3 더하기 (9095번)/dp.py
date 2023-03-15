import sys

T = int(sys.stdin.readline())

for _ in range(T):
    # 자연수 n 입력받기
    N = int(sys.stdin.readline())  
    # dp 리스트 초기화
    dp = [0] * (N+1)  
    # dp[1] 값 초기화
    dp[1] = 1  
    if N > 1:
        # dp[2] 값 초기화
        dp[2] = 2  
    if N > 2:
        # dp[3] 값 초기화
        dp[3] = 4  

    # dp[i] 값을 계산하는 반복문
    for i in range(4, N+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[N])  # dp[n] 값 출력
