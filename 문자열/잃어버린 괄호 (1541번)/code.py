import sys

A = sys.stdin.readline()

# '-' 기호를 기준으로 수식을 나눔
num = A.split('-')

# 결과값을 저장할 변수 N을 초기화
N = 0

# 첫 번째 '-' 이전의 문자열에서 '+' 기호를 기준으로 나누어서 각각의 숫자를 더함
for i in num[0].split('+'):
    N += int(i)

# 나머지 '-' 이후의 문자열에서는 '+' 기호를 기준으로 나누어서 각각의 숫자를 뺌
for i in num[1:]:
    for j in i.split('+'):
        N -= int(j)

print(N)
