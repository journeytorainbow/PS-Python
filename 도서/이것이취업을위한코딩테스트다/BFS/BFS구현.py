""" 143p """

from collections import deque

def bfs(graph, start, visited) : 

    need_visit = deque([start])

    visited[start] = True

    while need_visit :
        node = need_visit.popleft()
        print(node, end = ' ')

        for i in graph[node] :
            if not visited[i] :
                need_visit.append(i)
                visited[i] = True

visited = [False] * 9
# 2차원 리스트로 각 노드 연결된 정보를 표현
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

bfs(graph, 1, visited)