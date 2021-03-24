c = int(input())

for _ in range(c):
    data = list(map(int,input().split()))
    n = data[0]
    data = data[1:]
    mean = sum(data)/n

    total = 0
    for score in data:
        if score>mean:
            total+=1
    print('{0:0.3f}%'.format(total/n*100))
