def solution(board, moves): #board = 인형 표현(2차원 nxn 행렬), moves = 이동 순서
    doll = [] # 오른쪽 빈 stack
    answer = 0 #터트린 인형 갯수
    for move in moves:
        dol,board = pick_from_board(board, move) #board에서 pick 하기 dol = 인형, board= 인형 고른 후 board
        if dol != 0: # 인형이 없는 경우 0을 리턴 하므로 
            doll.append(dol) #기존 오른쪽 스택에 추가하기
        dol,distroy = check_result(doll) # 추가한 결과 두 인형이 연속인지 확인
        answer += distroy #
    return answer
def pick_from_board(board,move_num): # 인형 잡기 board : 인형 표현, move_num : 이동 위치
    doll = 0 # 인형 변수 초기화
    for row_num,num in enumerate(board): #행,순서(1부터 카운트)
        if num[move_num-1]!=0:
            doll = num[move_num-1]
            board[row_num][move_num-1] = 0
            break
    return doll,board

def check_result(doll):
    # 인형 연속 확인
    if len(doll) >=2: # 오른쪽 스택이 2이상
        input_doll = doll[-2:][0] # 나중에 넣은 인형
        current_doll = doll[-2:][1] # 바로 전 넣은 인형
        
        if input_doll == current_doll:
            doll.pop()
            doll.pop()
            return doll,2
    return doll,0
