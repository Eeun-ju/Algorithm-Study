t = int(input())

for i in range(t):
    n = int(input())
    data = format(n,'b')
    a = 0
    for j in range(len(data)-1,-1,-1):
        if data[j]=='1':
            print(a,end=' ')
        a+=1
    
