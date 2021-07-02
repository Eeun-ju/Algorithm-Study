n = int(input())
data = []
for _ in range(n*2-1):
	user_input = list(map(int,input().split()))
	data.append(user_input)
#print(data)

for i in range(1,n):#내려가기 row
	for j in range(i+1): #옆으로가기 idx
		if j == 0: #왼쪽에 붙어있음
			data[i][j] += data[i-1][j] 
		elif i == j:
			data[i][j] += data[i-1][j-1]
		else:
			data[i][j] += max(data[i-1][j-1],data[i-1][j])

for i in range(n,n*2-2):
	for j in range(len(data[i])):
		if j == 0 or 2*n-i-1 == j: #왼쪽에 붙어있음
			data[i][j] += max(data[i-1][j],data[i-1][j+1])
		else:
			data[i][j] += max(data[i-1][j+1],data[i-1][j])
print(max(data[-2])+data[-1][0])
