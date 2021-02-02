""" 111p """

import sys

n = int(sys.stdin.readline()) # 공간의 크기
plans = sys.stdin.readline().split() # 이동 계획

# 여행자의 최초 위치
x, y = 1, 1
move_types = ['L', 'R', 'U', 'D'] # 이동의 종류

# L, R, U, D (move_types랑 동일한 순서로 작성)
dx = [0, 0, -1, 1] # 세로로 움직이는 경우
dy = [-1, 1, 0, 0] # 가로로 움직이는 경우

# 이동 계획을 하나씩 확인
for plan in plans :
    # 이동 후 좌표 구하기
    for i in range(len(move_types)) :
        if plan == move_types[i] :
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n :
        continue
    x, y = nx, ny

print(x, y)