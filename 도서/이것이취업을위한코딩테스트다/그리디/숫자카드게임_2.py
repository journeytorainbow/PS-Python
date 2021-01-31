""" 96p - 답안2 : 이중 반복문 이용 """

import sys

n, m = map(int, sys.stdin.readline().split())

result = 0
for i in range(n) :
    # 한 행씩 입력 받기
    row = list(map(int, sys.stdin.readline().split()))
    # 현재 행에서 가장 작은 수 찾기
    min_value = 10001
    for data in row :
        min_value = min(min_value, data)
    
    # 가장 작은 수들 중 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력