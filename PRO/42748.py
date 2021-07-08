def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        data = array[commands[i][0]-1:commands[i][1]]
        data.sort()
        
        location = commands[i][2] - 1
        #print(data)
        answer.append(data[location])
    
    return answer
