n = int(input())
heights = list(map(int, input().split()))

line = [0] * n  
for i in range(n):
    # 현재 사람(i번째)보다 키가 큰 사람의 수
    count = 0  
    for j in range(n):
        if count == heights[i] and line[j] == 0:
            line[j] = i + 1
            break
        if line[j] == 0 or line[j] > i + 1:
            count += 1

print(*line)  
 