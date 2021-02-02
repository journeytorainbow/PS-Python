""" 118p : 전형적인 시뮬레이션 문제(삼성에서 자주 출제되는 대표적인 유형) """

import sys

n, m = map(int, sys.stdin.readline().split()) # 맵의 크기 (행, 열)

# 방문한 위치를 저장하기 위한 맵 크기의 리스트를 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 캐릭터의 현재 x, y좌표, 바라보고 있는 방향 입력 받기
x, y, direction = map(int, sys.stdin.readline().split())
d[x][y] = 1 # 캐릭터의 최초 위치 방문 처리

# 전체 맵 정보 입력 받기
array = []
for i in range(n) :
    array.append(list(map(int, sys.stdin.readline().split())))

# 북, 동, 남, 서 = 0, 1, 2, 3 => 이 순서대로 dx, dy를 작성해주자
# direcion을 이후에 인덱스로 사용하기 위함
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전 (북->서 , 서->남, 남->동, 동->북)
# 북, 동, 남, 서 = 0, 1, 2, 3 이므로 서->남, 남->동, 동->북으로
# 각각 회전 시에는 그냥 원래 방향에서 -1만 해주면되고,
# 북->서 회전인 경우에는 direction=3 해줘야 함
# direction은 아래 쪽에서 인덱스로 쓰일 예정
def turn_left() :
    global direction
    direction -= 1
    if direction == -1 : # 왼쪽으로 회전하기 전의 방향이 북쪽
        direction = 3 # 서쪽을 가리키는 3을 대입

# 시뮬레이션 시작
count = 1 # 유저가 방문한 칸의 수를 저장할 변수, 최초 위치도 카운트해줘야 하므로 초기값 1
turn_time = 0 # 한 위치에서 회전한 횟수 저장할 변수

while True :
    turn_left() # 왼쪽으로 회전
    # 회전 후, 해당 방향으로 이동 후의 좌표 구하기
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 이동 후의 좌표가 방문한적이 없으면서 육지인 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0 :
        d[nx][ny] = 1 # 방문 표시
        x = nx
        y = ny
        count += 1
        turn_time = 0 # 이동 후에는 회전 횟수 0으로 초기화
        continue
    else :
        turn_time += 1

    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4 :
        # 뒤로 한칸 이동한 좌표 구하기
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 뒤로 갈 수 있다면(바다가 아닌 경우)
        if array[nx][ny] == 0 :
            x = nx
            y = ny
            turn_time = 0 # 새로운 칸으로 이동했으므로 회전 횟수 0으로 초기화
        # 뒤가 바다인 경우(갈 수 없는 경우)
        else :
            break

print(count)