class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq_map = defaultdict(int)
        for h in hand:
            freq_map[h] += 1

        heap = list(freq_map.keys())
        heapq.heapify(heap)

        while heap:
            hand = heap[0]
            
            for i in range(hand, hand+groupSize):
                if i not in freq_map:
                    return False
                
                freq_map[i] -= 1
                if freq_map[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)
        
        return True