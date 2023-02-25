#소수 탐색 함수
def search_prime(prime):
    # 1보다 작은 경우 소수 아니므로 False
    if prime < 2:
        return False
    # 2부터 n-1까지 나누어 떨어지는 수 있으면 소수 아님
    for i in range(2, prime):
        if prime % i == 0:
            return False
    #해당하지 않으면 소수이므로 True
    return True

#메인 함수
def main():
    N = int(input())
    X = list(map(int, input().split()))

    cnt = 0
    for prime in X:
        #입력받은 수가 소수이면 cnt += 1
        if search_prime(prime):
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    main()