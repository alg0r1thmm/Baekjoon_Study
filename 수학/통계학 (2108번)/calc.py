import sys
from collections import Counter

def calc_mean(numbers):
    # 리스트의 산술평균을 계산하는 함수
    return round(sum(numbers) / len(numbers))

def calc_median(numbers):
    # 리스트의 중앙값을 계산하는 함수
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) // 2
    else:
        return numbers[len(numbers) // 2]

def calc_mode(numbers):
    # 리스트의 최빈값을 계산하는 함수
    count = Counter(numbers)
    mode = count.most_common()
    if len(numbers) > 1:
        if mode[0][1] == mode[1][1]:
            mode = mode[1][0]
        else:
            mode = mode[0][0]
    else:
        mode = mode[0][0]
    return mode

def calc_range(numbers):
    # 리스트의 범위를 계산하는 함수
    return max(numbers) - min(numbers)

# 입력값 받기
n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]

# 결과 출력
print(calc_mean(numbers))
print(calc_median(numbers))
print(calc_mode(numbers))
print(calc_range(numbers))
