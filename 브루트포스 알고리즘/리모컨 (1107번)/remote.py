move_channel = int(input()) # 이동하려는 채널
broken_btn = int(input()) # 고장난 버튼의 개수

if broken_btn > 0:
    borken_List = set(map(int, input().split())) # 고장난 버튼 리스트
    
else:
    borken_List = set()

# 숫자 버튼을 이용해 가장 최적의 수를 탐색
def possible(ch):
    if ch == 0:
        if 0 not in borken_List:
            return True
        else:
            return False
    while ch > 0:
        if ch % 10 in borken_List:
            return False
        ch //= 10
    return True

# 두가지 경우를 생각해야 함.
# 1. 채널 100부터 숫자 버튼으로 이동하는 단순한 경우
# 2. +, - 버튼으로만 이동하는 경우
# 두가지 경우에서 가장 최적의 수를 탐색
ans = abs(move_channel - 100)

for ch in range(1000001):
    if possible(ch):
        press = abs(ch - move_channel) + len(str(ch))
        if press < ans:
            ans = press

print(ans)