""" 115p : 상하좌우 문제와 유사 """

import sys

start = sys.stdin.readline() # 기사의 위치 입력받기 (col, row) : string
row, col = int(start[1]), int(ord(start[0])) - int(ord('a')) + 1

# 기사가 이동가능한 8가지 방향
move_types = [(1, 2), (1, -2), (-1, -2), (-1, 2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

count = 0

# 8가지 방향 각각에 대해 각 위치로 이동 가능한지 확인
for move in move_types :
    
    next_row = row + move[1]
    next_col = col + move[0]

    # 해당 위치로 이동이 가능(정원을 벗어나지 않는 위치)하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8 :
        count += 1

print(count)