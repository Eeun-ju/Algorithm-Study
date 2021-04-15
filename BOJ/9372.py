from collections import deque
import sys

input = sys.stdin.readline

def bfs(x):
    q = deque()
    q.append(x)
    c[x] = 1 # 방문
    cnt = 0
    while q :
        x = q.popleft()
        for nx in a[x]:
            if c[nx] == 0:
                c[nx] = 1
                cnt += 1
                q.append(nx)
    return cnt

testcase = int(input()) #tc개수

while testcase:
    n,m = map(int,input().split())

    a = [ [] for _ in range(n)]
    c = [0 for _ in range(n)]

    for _ in range(m):
        x,y = map(int,input().split())
        a[x-1].append(y-1)
        a[y-1].append(x-1)

    ans = 0
    for i in range(n):
        if c[i] == 0:
            ans += bfs(i)
    print(ans)
    testcase -= 1
