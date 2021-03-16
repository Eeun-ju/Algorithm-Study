n,m = map(int,input().split())
maxi = -1
for i in range(1,min(n,m)+1):
    if n%i==0 and m%i == 0:
        if maxi<i:
            maxi = i
print(maxi)
print(int(n*m/maxi))
