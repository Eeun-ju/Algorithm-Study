#RGB 거리
import sys
n = int(sys.stdin.readline().rstrip())
data = [[] for i in range(n)]
for i in range(n):
    if i == 0:
        cost = list(map(int,sys.stdin.readline().rstrip().split()))
        for j in range(3):
            data[0].append(cost[j])
    else:
        cost = list(map(int,sys.stdin.readline().rstrip().split()))
        for j in range(3):
            if j == 0:
                data[i].append(cost[j] + min(data[i-1][1],data[i-1][2]))
            if j == 1:
                data[i].append(cost[j] + min(data[i-1][0],data[i-1][2]))
            if j == 2:
                data[i].append(cost[j] + min(data[i-1][0],data[i-1][1]))
                               
print(min(data[n-1]))
