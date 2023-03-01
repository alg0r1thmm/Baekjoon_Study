import sys

#입력값 N, 카드 리스트, 입력값 M, 찾으려는 카드 리스트 입력
N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

#딕셔너리로 카드 리스트에서 각 숫자에 대한 카운트 진행
dic_card = {}

for i in cards:
    if i in dic_card:
        dic_card[i] += 1
    else:
        dic_card[i] = 1

result = []
for j in num:
    #찾으려는 카드가 딕셔너리에 있는 경우 카드의 개수 리스트에 추가
    if j in dic_card:
        result.append(dic_card[j])
    #없는 경우 0을 리스트에 추가
    else:
        result.append(0)

#결과 리스트에 대한 요소들 공백으로 구분 후 출력
print(' '.join(map(str, result)))
