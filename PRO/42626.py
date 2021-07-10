import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    count = 0

    while len(scoville) > 1:
        count += 1
        
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        
        heapq.heappush(scoville, f+s*2)
        if scoville[0] >= K:
            return count

    return -1
