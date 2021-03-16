a,b = map(int,input().split())

total = 0
d=[]
for i in range(1000):
    if len(d) >= b:
            break
    for j in range(i):
        d.append(i)

print(sum(d[a-1:b]))  

    
    
