""" 142p - 스택 사용하지 않고 재귀 이용 """

def dfs(graph, node, visited) :
    # 현재 노드를 방문 처리
    visited[node] = True
    print(node, end = ' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[node] :
        if not visited[i] :
            dfs(graph, i, visited)

# 각 노드가 방문된 정보를 표현
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