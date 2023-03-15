import sys

m = int(sys.stdin.readline().rstrip())
s = set()

for k in range(m):
    cmd = sys.stdin.readline().rstrip().split()
    
    # add 명령어를 처리
    if cmd[0] == "add":
        s.add(int(cmd[1]))
    # remove 명령어를 처리
    elif cmd[0] == "remove":
        s.discard(int(cmd[1]))
    # check 명령어를 처리
    elif cmd[0] == "check":
        if int(cmd[1]) in s:
            # check 명령어의 결과를 출력 
            sys.stdout.write("1\n")
        else:
            sys.stdout.write("0\n")
    # toggle 명령어를 처리
    elif cmd[0] == "toggle":
        if int(cmd[1]) in s:
            s.discard(int(cmd[1]))
        else:
            s.add(int(cmd[1]))
    # all 명령어를 처리
    elif cmd[0] == "all":
        # 집합을 1부터 20까지의 숫자로 초기화
        s = set(range(1, 21))
    # empty 명령어를 처리
    elif cmd[0] == "empty":
        # 집합을 빈 상태로 초기화
        s = set()
