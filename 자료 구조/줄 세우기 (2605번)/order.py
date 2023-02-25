#줄을 설 학생 입력
X = int(input())

#번호표 저장
order = list(map(int, input().split()))

#스택 초기화
stack = [0]

#학생 수 만큼 번호표 입력
for i in range(X):
    #처음 학생은 무조건 0번 인덱스
    if i == 0:
        order.append(i)
    #이외의 경우에는 스택 길이에 우선순위만큼 저장
    else:
        stack.insert(len(stack)-order[i], i)

#출력
for i in stack:
    print(i+1, end=' ')