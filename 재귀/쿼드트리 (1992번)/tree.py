import sys

# 입력 받기
n = int(sys.stdin.readline().strip()) # 영상의 크기
image = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)] # 영상

# 쿼드 트리 알고리즘 구현
def quad_tree(x, y, n):
    color = image[x][y] # 현재 영역의 색상
    # 현재 영역이 모두 같은 색으로 이루어져 있는 경우
    if all(image[i][j] == color for i in range(x, x+n) for j in range(y, y+n)):
        print(color, end="") # 해당 색상을 출력하고
        return # 종료
    # 현재 영역이 서로 다른 색으로 이루어져 있는 경우
    print("(", end="") # 괄호를 출력하고
    quad_tree(x, y, n//2) # 왼쪽 위 영역을 재귀적으로 처리
    quad_tree(x, y+n//2, n//2) # 오른쪽 위 영역을 재귀적으로 처리
    quad_tree(x+n//2, y, n//2) # 왼쪽 아래 영역을 재귀적으로 처리
    quad_tree(x+n//2, y+n//2, n//2) # 오른쪽 아래 영역을 재귀적으로 처리
    print(")", end="") # 괄호를 닫고

# 쿼드 트리 알고리즘 호출
quad_tree(0, 0, n)
