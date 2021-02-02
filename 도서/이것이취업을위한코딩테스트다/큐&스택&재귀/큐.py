# collections 모듈의 deque라이브러리 이용

from collections import deque

q = deque()

q.append(5)
q.append(3)
q.append(7)
q.append(6)

print(q)
print(q.popleft()) # 가장 먼저 입력된 값을 pop

q.append(4)
q.append(1)

print(q)