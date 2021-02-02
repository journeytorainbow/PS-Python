""" 교재에 없음"""

from collections import deque

graph = {
    1 : [2, 3, 8],
    2 : [1, 7],
    3 : [4, 5],
    4 : [3, 5],
    5 : [3, 4],
    6 : [7],
    7 : [6, 8],
    8 : [1, 7]
}

visited = deque()
need_visit = deque()

need_visit.append(1)

while need_visit :
    node = need_visit.popleft()

    if node not in visited :
        visited.append(node)
        need_visit.extend(graph[node])

print(list(visited))