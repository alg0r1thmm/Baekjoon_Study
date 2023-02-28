import sys

N = int(sys.stdin.readline())

num = 1666 #영화 제목 뒤에 붙일 수 666
count = 0 #0번째 인덱스부터 시작하므로 count = 0 초기화

while True:
    #666 이 들어가는 경우
    if '666' in str(num):
        #count 1 증가
        count += 1
    # count와 입력한 N 값이 같아지는 경우
    if count == N:
        #출력
        print(num)
        break
    #다음 숫자로 이동
    num += 1