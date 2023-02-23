#에라토스테네스의 체 구현

n = int(input())
numbers = list(map(int, input().split()))

#두 수 사이의 최대값 구하기
max_result = 0 #주어진 n개의 수들 중 최댓값 저장
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        diff = abs(numbers[i] - numbers[j])
        if diff > max_result:
            max_result = diff

#최대공약수 구하기
result = 1 #최대공약수를 저장할 변수 1로 초기화
for i in range(2, max_result+1):
    if max_result % i == 0:
        temp = numbers[0] % i
        for j in range(1, n):
            if numbers[j] % i != temp:
                break
        else:
            result = i

#최대공약수 출력
print(result)