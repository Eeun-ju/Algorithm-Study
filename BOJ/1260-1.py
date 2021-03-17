# DFS 예제
from collections import deque


def dfs(graph, v, visited):

    visited[v] = True
    print(v, end= " ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)
def bfs(graph, v, visited):
    
    queue = deque([v])

    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v,end = " ")

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n,m,v = map(int,input().split())

graph = [[] for i in range(n+1)]
#print(graph)
for i in range(m):
    start, end = map(int,input().split())

    graph[start].append(end)
    graph[end].append(start)


visited_DFS = [False]*(n+1)
visited_BFS = [False]*(n+1)

dfs(graph,v,visited_DFS)
print()
bfs(graph,v,visited_BFS)

