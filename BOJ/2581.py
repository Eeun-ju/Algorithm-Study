m = int(input())
n = int(input())
total = 0
mini = 10000
for i in range(m,n+1):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count += 1
    if count == 2:
        if mini>=i:
            mini = i
        total += i
if mini!=10000:
    print(total)
    print(mini)
else:
    print(-1)
    
