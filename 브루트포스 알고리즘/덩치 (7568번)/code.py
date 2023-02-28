N = int(input())
my_list = []

# 입력값 처리
for i in range(N):
    x = list(map(int, input().split()))
    my_list.append(x)

# 덩치 등수 계산
for i in range(N):
    rank = 1
    for j in range(N):
        if my_list[i][0] < my_list[j][0] and my_list[i][1] < my_list[j][1]:
            rank += 1
    print(rank, end=' ')
