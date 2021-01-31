""" 92p - 답안1 """

import sys


n, m, k = map(int, sys.stdin.readline().split())
#  입력 받은 수들 내림 차순 정렬
n_list = sorted(list(map(int, sys.stdin.readline().split())), reverse = True)

first = n_list[0] # 가장 큰수
second = n_list[1] # 두 번째로 큰수

result = 0

while True :
    for i in range(k) : # 가장 큰수를 k번 더하기
        if m == 0 : # 0이면 반복문 탈출
            break
        result += first
        m -= 1 # 한 번 더할 때마다 1씩 빼기
    if m == 0 : # 0이면 반복문 탈출
        break
    result += second # 두번째 큰수 1번 더하기
    m -= 1 # 한 번 더할 때마다 1씩 빼기

print(result) # 최종 답안 출력