# 파이썬에서 스택은 리스트와 pop(), append() 이용해 구현

stack = []

stack.append(5)
stack.append(3)
stack.append(7)
stack.append(6)

print(stack) # [5, 3, 7, 6]
print(stack.pop()) # 6, 가장 나중 추가된 원소를 pop
print(stack[::-1]) # [7, 3, 5]