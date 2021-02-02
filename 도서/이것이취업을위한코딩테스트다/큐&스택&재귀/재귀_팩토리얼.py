# 팩토리얼 함수 구현

# 반복문 이용
def factorial_iterative(n) :
    result = 1
    for i in range(1, n+1) :
        result *= i
    return result

print("반복문 이용", factorial_iterative(5))

# 재귀 이용
def factorial_recursive(n) :
    if n <= 1 :
        return 1
    
    return n * factorial_recursive(n - 1)

print("재귀 이용", factorial_recursive(5))