""" 교재에 없는 내용 - 스택 이용 """

graph = {
    1 : [8, 3, 2],
    2 : [7, 1],
    3 : [5, 4],
    4 : [5, 3],
    5 : [4, 3],
    6 : [7],
    7 : [8, 6],
    8 : [7, 1]
}

start = 1

visited = [] # 큐
need_visit = [] # 스택

need_visit.append(start)

while need_visit :
    node = need_visit.pop()
    if node not in visited :
        need_visit.extend(graph[node])
        visited.append(node)

print(visited)