def result(n, a, s):
    if s>= n:
        s - n -1
    #정렬할 리스트 길이만큼 반복
    for i in range(n):
        if s==0 or a == sorted(a, reverse=True):
            break
        #정렬할 범위 내에서 가장 큰 값의 인덱스를 초기값으로 설정
        idx = i
        #정렬할 범위 내에서 최대 s번만큼 탐색
        for j in range(i+1, min(n, i+s+1)):
            #가장 큰 값을 찾아서 인덱스 저장
            if a[j] > a[idx]:
                idx = j
        if idx != i:
            #정렬할 범위 내에서 가장 큰 값의 인덱스부터 i까지 역순으로 반복
            for j in range(idx, i, -1):
                #바로 뒤의 값과 교환
                a[j], a[j-1] = a[j-1], a[j]
                s -=1
            
n = int(input())
a = list(map(int, input().split()))
s = int(input())

result(n, a, s)

print(*a) # 리스트 a 출력