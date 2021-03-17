n,k = map(int,input().split())

data = []
for i in range(n):
    data.append(input())
train = ['a','n','t','i','c']
test = []
if k<5:
    print(0)
else:
    for i in range(n):
        df = data[i]
        a = []
        for j in range(len(df)):
            if df[j] not in train:
                a.append(df[j])
    
        a = list(set(a))
        test.append(a)

    
    
