from collections import deque
import sys

input = sys.stdin.readline

#동서남북 방향
dx = [1,-1,0,0]
dy = [0,0,-1,1]

n,l,r = map(int,input().split())
s = []

for i in range(n):
    s.append(list(map(int,input().split())))
    
result = 0
#BFS사용

def bfs(i,j):
    q = deque()
    q.append([i,j]) #방문 좌표 추가
    
    temp = []
    temp.append([i,j])

    while q:
        
        x,y = q.popleft() #q 좌표 
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx>=0 and nx<n and ny>=0 and ny<n and visit[nx][ny] == 0:
                if l<=abs(s[nx][ny] - s[x][y]) <= r:
                    visit[nx][ny] = 1
                    q.append([nx,ny])
                    temp.append([nx,ny])
    return temp


while True:
    visit = [[0] * n for _ in range(n)]
    isTrue = False
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 0: #방문하지 않았다면
                visit[i][j] = 1 #방문한다.
                temp = bfs(i, j)
                if len(temp) > 1: #인구 이동
                    isTrue = True
                    num = sum([s[x][y] for x, y in temp]) // len(temp)
                    for x, y in temp:
                        s[x][y] = num
    if not isTrue:
        break
    result += 1
print(result)
