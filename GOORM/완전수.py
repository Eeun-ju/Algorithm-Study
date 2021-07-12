a,b = map(int,input().split())
num = a
while num <= b:
    result = 0
    for i in range(1,num):
        if num%i == 0:
            result += i
    if num == result:
        print(num,end=' ')
    num += 1
