#깊이 우선 탐색
def solution(numbers, target):
    answer = dfs(0, numbers, target)
    return answer

#재귀로 불러오기
def dfs(result,numbers,target):
    if len(numbers) == 1:
        if result + numbers[0] == target or result-numbers[0] == target:
            return 1
        else:
            return 0
    else:
        return dfs(result+numbers[0],numbers[1:],target) + dfs(result-numbers[0],numbers[1:],target)
    

    
    
    
