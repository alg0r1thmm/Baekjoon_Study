import sys

a = int(sys.stdin.readline())

list = []

#입력받은 숫자만큼 반복시키며 리스트에 값 추가
for i in range(a):
    b = int(sys.stdin.readline())
    list.append(b)

#reverse=False 이용해서 오름차순 정렬
c = sorted(list, reverse=False)

#출력
for i in range(a):
    print(c[i])