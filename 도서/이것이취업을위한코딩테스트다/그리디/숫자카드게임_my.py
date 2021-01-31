""" 96p - 나의 답안 : min()함수 이용 """

import sys

n, m = map(int, sys.stdin.readline().split())
card_list = []

for i in range(n) :
    card_list.extend([list(map(int, sys.stdin.readline().split()))])

max_val = 0 # 각 행의 가장 작은 수 중에서 가장 큰 수를 저장할 변수
temp = 0

for row in card_list :
    temp = min(row) # 매 반복마다 각 행에서 가장 작은 수 저장
    if max_val < temp : # 다음 행의 가장 작은 수가 현재 max_val보다 크면 그 값으로 갱신
        max_val = temp

print(max_val) # 최종 답안 출력