import sys

n, m = map(int, sys.stdin.readline().split())

nh = set()
ns = set()

# 입력값을 set에 추가
for _ in range(n):
    nh.add(sys.stdin.readline().strip())
for _ in range(m):
    ns.add(sys.stdin.readline().strip())

nh_and_seen = sorted(list(nh & ns))

print(len(nh_and_seen))
print('\n'.join(nh_and_seen))
