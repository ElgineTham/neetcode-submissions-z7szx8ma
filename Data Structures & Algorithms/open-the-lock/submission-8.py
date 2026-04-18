class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        deadset = set()
        for d in deadends:
            deadset.add(d)

        seen = set()
        q = deque()
        q.append("0000")
        seen.add("0000")
        turns = 0

        while q:
            for i in range(len(q)):
                comb = q.popleft()
                if comb == target:
                    return turns
                for j in range(4):
                    dig_1 = str((int(comb[j]) + 1) % 10)
                    dig_2 = str((int(comb[j]) - 1 + 10) % 10)
                    child_1 = comb[:j] + dig_1 + comb[j+1:]
                    child_2 = comb[:j] + dig_2 + comb[j+1:]
                    if child_1 not in seen and child_1 not in deadset:
                        q.append(child_1)
                        seen.add(child_1)
                    if child_2 not in seen and child_2 not in deadset:
                        q.append(child_2)
                        seen.add(child_2)
            
            turns += 1
        
        return -1