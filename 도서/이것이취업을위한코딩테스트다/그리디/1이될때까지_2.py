""" 99p - 답안2 : 좀 더 효율적인 코드 """

import sys

n, k = map(int, sys.stdin.readline().split())

count = 0

while True :
    target = (n // k) * k
    count += (n - target) # n이 k의 배수가 되도록 한 번에 빼기 (일일이 1씩 빼는게 아니라)
    n = target

    # n이 k보다 작을 때 (더이상 나눌 수 없을 때) 반복문 탈출
    if n < k :
        break

    # k로 나누기
    n //= k
    count += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
count += (n - 1)
print(count)