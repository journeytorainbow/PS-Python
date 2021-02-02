""" 113p : 3중 반복문 이용 """ 
# 완전 탐색(Brute Forcing)유형이기도 함
# 00000부터 1씩 증가시켜가면서 n5959까지 전부 확인하면 됨

import sys

n = int(sys.stdin.readline()) # 시간 입력 받기
 
count = 0
for i in range(n+1) : # 시간
    for j in range(60) : # 분
        for k in range(60) : # 초
            # 매 시각 마다 3이 포함되어있는 지 확인
            if '3' in str(i) + str(j) + str(k) : # 매시각을 문자열로 바꾸기
                count += 1

print(count)