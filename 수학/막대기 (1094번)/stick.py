import sys

def count_one(N): # 이진법으로 변환하여 1의 개수를 세는 함수
    binary = bin(N)[2:] # '0b'를 제거
    return binary.count('1') # 1의 개수 반환

N = int(sys.stdin.readline()) # 10진수 숫자 입력
result = count_one(N) # 1의 개수
print(result)
