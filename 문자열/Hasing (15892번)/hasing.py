def hashing(s: str) -> int:
    # M과 R을 상수로 정의
    M = 1234567891
    R = 31
    hash_value = 0
    # 문자열의 각 문자에 대해 hash 값을 계산
    for i, c in enumerate(s):
        # 각 문자에 대해 R^i 값을 곱한 후, M으로 나눈 나머지를 더해 hash_value에 누적
        hash_value += (ord(c) - ord('a') + 1) * (R ** i)
        hash_value %= M
    return hash_value

# 입력값 처리
n = int(input())
s = input().strip()
# 계산된 hash 값을 출력
print(hashing(s))

#hash(s) = (s[0] × R⁰ + s[1] × R¹ + ... + s[n-1] × R^(n-1)) mod M