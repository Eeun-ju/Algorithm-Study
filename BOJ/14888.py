import itertools

def divi(z,x):
    re = 0
    if z<0:
        re = abs(z)//x
        return re*(-1)
    else:
        re = z//x
        return re


def y(a,dd,q):
    res=a[0]
    for i in range(0,len(dd)):
        if dd[i]=='0':
            res+=a[i+1]
        elif dd[i]=='1':
            res-=a[i+1]
        elif dd[i]=='2':
            res*=a[i+1]
        elif dd[i]=='3':
            res=divi(res,a[i+1])
    q.append(res)
      
n = int(input())
data = list(map(int,input().split()))
op = list(map(int,input().split()))
# 덧셈, 뺄셈, 곱셈, 나눗셈

result = []

for i in range(0,4):
    for j in range(0,op[i]):
        result.append(str(i))
#print(result)   

yy = list(map(''.join,itertools.permutations(result,len(result))))
#print(yy)
c=[]
yy = list(set(yy))

for i in range(0,len(yy)):
    y(data,yy[i],c)
print(max(c))
print(min(c))
