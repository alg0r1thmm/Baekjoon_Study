import sys

#리스트의 크기 N 입력
N = int(sys.stdin.readline())
#리스트 A set으로 입력
A = set(map(int, sys.stdin.readline().split()))
#찾으려는 값의 개수 입력
M = int(sys.stdin.readline())
#찾으려는 값 입력
X = list(map(int, sys.stdin.readline().split()))

for i in X:
    #X가 A에 있는 경우 1 출력
    if i in A:
        print(1)
    #X가 A에 없는 경우 0 출력
    else:
        print(0)
