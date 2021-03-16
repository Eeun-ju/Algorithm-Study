n = int(input())
data = list(map(int,input().split()))

total = 0

for i in data:
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count +=1

    if count == 2:
        total += 1
print(total)
