#플로이드 워셜 알고리즘

import sys
v,e = map(int,input().split())
inf = 10000*v + 1
distance = [[inf for _ in range(v+1)] for _ in range(v+1)]


for _ in range(e):
    start, end, dist = map(int,sys.stdin.readline().split())
    distance[start][end] = dist

for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])


mini = inf
for i in range(1,v+1):
    mini = min(mini, distance[i][i])

if mini == inf:
    print(-1)
else:
    print(mini)
