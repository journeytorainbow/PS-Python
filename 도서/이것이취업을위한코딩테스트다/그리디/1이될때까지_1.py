""" 99p - 답안1 : 단순하게 푸는 방법 """

import sys

n, k = map(int, sys.stdin.readline().split())

count = 0

# n이 k보다 이상이면 k로 계속 나누기
while n >= k :
    # n이 k로 나눠떨어지지 않는다면 n에서 1씩 빼기
    while n % k != 0 :
        n -= 1
        count += 1
    # n을 k로 나누기
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1 :
    n -= 1
    count += 1

print(count)