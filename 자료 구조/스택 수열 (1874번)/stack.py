import sys
# 첫 줄에는 수열의 길이 n을 입력받
n = int(sys.stdin.readline())
# 스택 리스트 초기화
stack = []
# 결과 리스트 초기화
result = []
# cnt 변수를 이용하여 1부터 n까지의 수를 스택에 push
cnt = 1

# 1부터 n까지 반복하여 수열을 확인
for i in range(1, n+1):
    # 수열 입력
    num = int(sys.stdin.readline())
    # cnt부터 num까지 스택에 push 후 '+' 문자를 결과 리스트에 추가
    while cnt <= num:
        stack.append(cnt)
        result.append('+')
        cnt += 1
    # 스택의 top이 num과 같으면 pop 후 '-' 문자를 결과 리스트에 추가
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    # 스택의 top이 num과 다르면 'NO'를 출력 후 프로그램을 종료
    else:
        print('NO')
        exit(0)
# 결과 리스트에 저장된 문자열을 개행문자를 이용하여 출력
print('\n'.join(result))
