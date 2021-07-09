def solution(money):
    answer = 0
    a = money[:len(money)-1]
    a[1] = max(a[0],a[1])
    for i in range(2,len(a)):
        a[i] = max(a[i-1],a[i-2]+a[i])
    b = money
    b[0]=0
    b[1] = max(b[0],b[1])
    for i in range(2,len(b)):
        b[i] = max(b[i-1],b[i-2]+b[i])
    return max(a+b)
