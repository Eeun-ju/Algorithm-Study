def solution(price, money, count):
    for c in range(1,count+1):
        money -= price*c

    if money >=0:
        return 0
    else:
        answer = (-1)*money
        return answer


'''

def solution(price, money, count):
    return abs(min(money - sum([price*i for i in range(1,count+1)]),0)

'''
