import sys

k,n = map(int,input().split())
array = []
for i in range(k):
    array.append(sys.stdin.readline().rstrip())
#['802','743']

start = 0
end = int(max(array))

result = 0

while(start <=end):
    total = 0
    mid = (start + end)//2

    for x in array:
        x = int(x)

        if x > mid:
            total += x//mid
    if total < n:
        end = mid - 1
    else:
        result = mid
        start = mid+1

print(result)


