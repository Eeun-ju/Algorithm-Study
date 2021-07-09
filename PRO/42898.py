def solution(m, n, puddles):
    answer = 0
    d=[[0]*(m+1) for _ in range(n+1)]
    d[1][1]=1
    for i in range(1,n+1): #n이 행
        for j in range(1,m+1): #m 열
            if i==1 and j==1:   
                continue
            if [j,i] in puddles:
                d[i][j]=0
            else:
                d[i][j]=(d[i-1][j]+d[i][j-1])%1000000007
    return d[n][m]
