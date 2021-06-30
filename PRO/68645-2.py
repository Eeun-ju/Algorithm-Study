def solution(n):
    #answer = [[0 for _ in range(1,i+1)] for i in range(1,n+1)]
    answer = [[0]*n for _ in range(n)]
    
    x,y = -1,0 #좌표 초기화 => 처음 시작은 아래로 내려감
    num = 1

    for i in range(n):
        for j in range(i,n):
            if i%3 == 0: #삼각형 면이 3개씩
                x += 1 # 내려가기
            elif i%3 == 1:
                y += 1 # 옆으로 이동
            else:
                x-=1 # 위로, 옆으로
                y-=1
            answer[x][y] = num #위치에 num값 추
            num+=1
    print(answer)
    return sum(answer,[])
