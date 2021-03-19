import sys

k,n = map(int,input().split())
array = []
for i in range(k):
    array.append(int(sys.stdin.readline().rstrip()))


start = 1
end = max(array)


while(start <=end):
    total = 0
    mid = (start + end)//2
    
    if mid == 0:
        end = 1
        break
    
    for x in array:
        
        total += x//mid
        
    if total >= n:
        start = mid + 1
    else:
        end = mid-1

print(end)


