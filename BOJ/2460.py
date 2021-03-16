total = 0
maxi = -1
for i in range(10):
    off,on = map(int,input().split())
    total = total + on - off
    if total >= maxi:
        maxi = total

print(maxi)
