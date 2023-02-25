import sys

def sort_points():
    #입력 받기
    n = int(sys.stdin.readline()) #점의 개수
    points = [] #좌표를 저장할 리스트
    for i in range(n):
        x, y = map(int, sys.stdin.readline().split()) #좌표 입력 받기
        points.append((x, y)) #좌표 리스트에 추가하기
    
    #좌표 정렬하기
    #y 좌표를 기준으로 오름차순 정렬, y 좌표가 같은 경우 x 좌표를 기준으로 오름차순 정렬
    points.sort(key=lambda point: (point[1], point[0])) 

    #정렬된 좌표 출력하기
    for point in points:
        # 정렬된 좌표 출력하기
        print(point[0], point[1])
