""" 92p - 답안2 """

import sys

n, m, k = map(int, sys.stdin.readline().split())
#  입력 받은 수들 내림 차순 정렬
n_list = sorted(list(map(int, sys.stdin.readline().split())), reverse = True)

first = n_list[0] # 가장 큰수
second = n_list[1] # 두번째로 큰수

result = 0
count_first = (m // (k+1)) * k + (m % (k+1)) # 가장 큰수가 더해지는 총 횟수
# count_second = (m // (k+1)) # 두번째로 큰수가 더해지는 총 횟수

# result = count_first * first + count_second * second
result += (count_first) * first # 가장 큰수의 총합 더하기
result += (m - count_first) * second # 두번째로 큰수의 총합 더하기

print(result) # 최종 답안 출력