""" 96p - 답안1 : min()함수 이용 """

import sys

n, m = map(int, sys.stdin.readline().split())

result = 0
# 한 줄(행)씩 입력 받으면서 확인
for i in range(n) :
    row = list(map(int, sys.stdin.readline().split()))
    # 현재 행에서 가장 작은 수 찾기
    min_value = min(row)
    # 가장 작은 수들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력