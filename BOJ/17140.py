from collections import Counter

r,c,k = map(int,input().split())
data = []
for _ in range(3):
    data.append(list(map(int,input().split())))

r = r - 1
c = c - 1
    
time = 0
while time <= 100: # 시간이 100인 경우에도 확인 해야한다.


    if r<len(data) and c<len(data[0]) and data[r][c] == k: # 정답 출력하기
        print(time)
        break

    # transpose 하는지
    col = False

    # 열 연산일 경우 transpose
    if len(data)< len(data[0]):
        col = True
        data = list(zip(*data))
        
    # 행 연산하기
    max_len=0
    tmp_a = []

    # 전체 행 연산
    for n_row in data:
        ct = Counter(n_row) #counter 숫자:개수 만들기

        if ct.get(0): # 0은 카운팅 하지 않음
            del ct[0]
            
        num_cnt = list(map(list,ct.items()))
        num_cnt.sort(key=lambda x : (x[1],x[0]))
        
        tmp_a.append(list(sum(num_cnt,[]))[:100])
        max_len = max(max_len,len(tmp_a[-1]))

    for i in range(len(tmp_a)):
        if len(tmp_a[i]) <max_len:
            tmp_a[i] += [0]*(max_len - len(tmp_a[i]))
    data = tmp_a

    if col:
        data = list(zip(*data))
    time += 1

    
if time > 100:
    print(-1)
                

    
