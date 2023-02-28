N = int(input())
stack = []

for i in range(N):
    X = int(input())
    #X값이 0인 경우 pop
    if X == 0:
        stack.pop()
    #이외의 경우에는 append로 추가
    else:
        stack.append(X)

#총 합계 출력
print(sum(stack))
