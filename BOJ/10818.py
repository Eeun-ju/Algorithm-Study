n = int(input())
array = list(map(int,input().split()))

mini = 1000000
maxi = -1000000
for i in range(n):
    if mini>=array[i]:
        mini = array[i]
    if maxi<=array[i]:
        maxi = array[i]

print(mini,maxi)
