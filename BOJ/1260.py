import sys
from collections import deque

sys.setrecursionlimit(1000000)

def DFS(v):

    print(str(v),end=" ")

    if v == M:
        return
    else:
        for i in range(1,N+1):
            if MAP[v][i] == 1 and check[i] is False:
                check[i] = True
                DFS(i)

def BFS(v):
    Q = deque([])
    Q.append(v)
    print(Q)
    while Q:
        x = Q.popleft()

        if check_BFS[x] is False:
            check_BFS[x] = True
            print(x, end=" ")

            for i in range(1,N+1):
                if MAP[x][i] == 1 and check_BFS[i] is False:
                    Q.append(i)


N,M,V = map(int,input().split())
MAP = [[0] *(N+1) for _ in range(N+1)]

check = [False]*(N+1)
check_BFS = [False]*(N+1)

for i in range(M):
    start, end = map(int, input().split())

    MAP[start][end] = 1
    MAP[end][start] = 1
    # 두 정점 사이에 간선은 양방향

check[V] = True

DFS(V)
print()
BFS(V)




