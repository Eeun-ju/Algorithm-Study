import sys
sys.setrecursionlimit(10000)

def dfs(graph,v,visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    start, end = map(int,sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

count = 0

for j in range(1,n+1):
    if not visited[j]:
        dfs(graph,j,visited)
        count+=1
print(count)
