#math 라이브러리 없이 구현
n, m = map(int, input().split())

# 분자 계산
top = 1
for i in range(n, n-m, -1):
    top *= i

# 분모 계산
bottom = 1
for i in range(m, 0, -1):
    bottom *= i

# 조합 계산
result = top // bottom

print(result)