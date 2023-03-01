from collections import Counter

X = int(input())

book = []

for i in range(X):
    Y = input().strip()
    book.append(Y)

#cnt에 Counter 사용해서 책 제목별 등장 횟수 계산
cnt = Counter(book)

#등장 횟수 가장 많은 책 제목 찾기
best = max(cnt.keys(), key=lambda x: cnt[x])

#등장 횟수가 가장 많은 책 제목들을 찾기
best_result = [title for title, count in cnt.items() if count == cnt[best]]

#사전 순으로 가장 앞서는 책 제목 찾기
result = sorted(best_result)[0]

print(result)
